import bs4
import sys
from pathlib import Path
from ruamel.yaml import YAML
from collections import ChainMap
from typing import Optional

yaml = YAML()
yaml.explicit_start = True

ALLOWED_CLASSES = [
    "powerdns.interface.PDNSServer",
    "powerdns.interface.PDNSZone",
    "powerdns.interface.PDNSEndpoint",
]

TYPE_MAPPING_YAML = {"str": "string", "list": "array", "bool": "boolean", "int": "number"}


class Parameters:
    name: str
    type_: str
    description: str
    required: bool
    default: Optional[str]

    def __init__(self, name, type_, description, required, default=None):
        self.name = name
        self.type_ = TYPE_MAPPING_YAML.get(type_, type_)
        self.description = description
        self.required = required
        self.default = default

    @property
    def parameters(self):
        content = {
            "type": self.type_,
            "description": self.description,
            "required": self.required,
        }
        if self.default:
            content.update({"default": self.default})
        return {self.name: content}


class Template:
    name: str
    description: str
    script_name: str = ""
    call: str = "api"

    def __init__(self, action_path, content, parent_name):
        self.action_path = Path(action_path)
        self.content = content
        self.parameters = [self.add_server_id(), self.add_timeout()]

        if parent_name == "powerdns.interface.PDNSZone":
            self.parameters.append(self.add_zone_name())

        if parent_name == "powerdns.interface.PDNSEndpoint":
            self.call = "_api"

    @staticmethod
    def add_zone_name():
        return Parameters(
            name="zone_name",
            type_="string",
            description="Zone's canonical name to get details.",
            required=True,
        )

    @staticmethod
    def add_server_id():
        return Parameters(
            name="server_id",
            type_="string",
            description="Server name to query.",
            required=True,
            default="localhost",
        )

    @staticmethod
    def add_timeout():
        return Parameters(
            name="response_timeout",
            type_="number",
            description="Time to wait for a response from PowerDNS",
            default=5,
            required=False,
        )

    @property
    def class_name(self):
        return self.name.title().replace("_", "")

    def write_yaml(self):
        content = {
            "name": f"{self.script_name or self.name}",
            "runner_type": "python-script",
            "description": self.description,
            "entry_point": f"{self.script_name or self.name}.py",
            "parameters": dict(ChainMap(*map(lambda x: x.parameters, self.parameters))),
        }
        with open(self.action_path / Path(f"{self.script_name or self.name}.yaml"), "w") as fp:
            yaml.dump(content, fp)

    def to_py(self):
        return f"""from lib.base import PowerDNSClient


class {self.class_name}(PowerDNSClient):
    def _run(self, *args, **kwargs):
        return self.{self.call}.{self.name}(*args, **kwargs)
"""

    def write_py(self):
        content = self.to_py()
        with open(self.action_path / Path(f"{self.script_name or self.name}.py"), "w") as fp:
            fp.write(content)

    def parse(self):
        raise NotImplementedError

    def write(self):
        self.parse()
        self.write_yaml()
        self.write_py()


class Class(Template):
    def _parse_params(self, parameters, params_default_values):
        for parameter in parameters:
            parameter_name = "rrset_" + parameter.find("strong").text
            required = True
            for item in params_default_values:
                if item.find("span", {"class": "n"}).text == parameter_name and item.find(
                    "span", {"class": "o"}
                ):
                    required = False
            try:
                description = parameter.find("p").text.split("–")[-1].strip().replace("\n", " ")
            except AttributeError:
                description = parameter_name

            self.parameters.append(
                Parameters(
                    name=parameter_name,
                    type_=parameter.find("em").text,
                    description=description,
                    required=required,
                )
            )

    def parse(self):
        self.name = self.content.find("dt", {"class": "sig sig-object py"}).get("id")
        parameters = self.content.find("ul", {"class": "simple"}).find_all("li")
        params_default_values = self.content.find_all("em", {"class": "sig-param"})

        self._parse_params(parameters, params_default_values)


class Method(Template):
    def __init__(self, action_path, content, parent_name, rrsets_params):
        super().__init__(action_path, content, parent_name)
        self.rrsets_params = rrsets_params

    def _parse_params(self, parameters, params_default_values):
        add_rrset = False
        require_rrset = True

        for parameter in parameters:
            parameter_name = parameter.find("strong").text
            required = True

            for item in params_default_values:
                if item.find("span", {"class": "n"}).text == parameter_name and item.find(
                    "span", {"class": "o"}
                ):
                    required = False
                    if parameter_name == "rrsets":
                        require_rrset = False

            if parameter_name == "rrsets":
                add_rrset = True
                continue

            try:
                description = parameter.find("p").text.split("–")[-1].strip().replace("\n", " ")
            except AttributeError:
                description = parameter_name

            self.parameters.append(
                Parameters(
                    name=parameter_name,
                    type_=parameter.find("em").text,
                    description=description,
                    required=required,
                )
            )

        if add_rrset:
            for param in rrset_params:
                if not require_rrset:
                    param.required = require_rrset
            self.parameters += rrset_params

    def parse(self):
        self.name = self.content.find("dt", {"class": "sig sig-object py"}).get("id").split(".")[-1]
        self.description = self.content.find("dd").find("p").text
        params_default_values = self.content.find_all("em", {"class": "sig-param"})

        try:
            # if only one param, it's not li but p
            parameters = self.content.find("dl", {"class": "field-list simple"}).find_all(
                "li"
            ) or self.content.find("dd", {"class": "field-odd"}).find_all("p")
        except AttributeError:  # there is no args at all
            parameters = []

        self._parse_params(parameters, params_default_values)


class Property(Template):
    def parse(self):
        self.name = self.content.find("span", {"class": "sig-name descname"}).text
        self.description = self.content.find("dd").find("p").text
        self.script_name = f"get_{self.name}"

    def to_py(self):
        pytext = f"""from lib.base import PowerDNSClient


class {self.class_name}(PowerDNSClient):
    def _run(self):
"""

        # iterate and cast items to strings for some api calls.
        if self.name in ["zones", "servers"]:
            single = self.name[:-1]
            pytext += (
                f"        return [str({single}) for {single} in self.{self.call}.{self.name}]\n"
            )
        else:
            pytext += f"        return self.{self.call}.{self.name}\n"
        return pytext


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(
            """
Usage: python <path to powerdns doc> <path to stackstorm action dir>

Example:
python generate_pack.py ~/python-powerdns/docs/html/interface.html ~/stackstorm-powerdns/actions/
"""
        )
        sys.exit()

    with open(sys.argv[1]) as handle:
        html_documentation = handle.read()

    action_path = sys.argv[2]
    parsed_documentation = bs4.BeautifulSoup(html_documentation, "html.parser")
    all_cls = parsed_documentation.find_all("dl", {"class": "py class"})

    # We need to retrieive first all parameters for RRSets so we can later add it to each action
    # that needs it
    for cls in all_cls:
        cls_name = cls.find("dt", {"class": "sig sig-object py"}).get("id")
        if cls_name != "powerdns.interface.RRSet":
            continue
        parsed_cls = Class(action_path, cls, cls_name)
        parsed_cls.parse()
        rrset_params = parsed_cls.parameters

    for cls in all_cls:
        cls_name = cls.find("dt", {"class": "sig sig-object py"}).get("id")
        if cls_name not in ALLOWED_CLASSES:
            continue

        cls_methods = cls.find_all("dl", {"class": "py method"}) or []
        cls_properties = cls.find_all("dl", {"class": "py property"}) or []

        for cls_property in cls_properties:
            Property(action_path, cls_property, cls_name).write()

        for cls_method in cls_methods:
            Method(action_path, cls_method, cls_name, rrset_params).write()
