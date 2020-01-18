
from st2common import log as logging
from st2common.runners.base_action import Action
import requests, json

__all__ = ["PowerDNSClient"]

LOG = logging.getLogger(__name__)


class PowerDNSClient(Action):

    def __init__(self, config):
        super(PowerDNSClient, self).__init__(config)

    # CODE TO MANAGE POWERDNS ZONES

    def zones_list(self, server_hostname, api_key):
        url = "http://{server_hostname}:8081/api/v1/servers/localhost/zones".format(
            server_hostname=server_hostname)
        headers = {'X-API-Key': api_key, 'Content-Type': 'application/json'}
        response = requests.request("GET", url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            error = "Something odd happened, response code was {code}".format(code=response.status_code)
            raise ValueError(error)

    def zone_get(self, server_hostname, api_key, name):
        name = self.make_canonical(name)
        url = "http://{server_hostname}:8081/api/v1/servers/localhost/zones/{zone}".format(
            server_hostname=server_hostname, zone=name)
        headers = {'X-API-Key': api_key, 'Content-Type': 'application/json'}
        response = requests.request("GET", url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            error = "Something odd happened, response code was {code}".format(code=response.status_code)
            raise ValueError(error)

    def zone_create(self, server_hostname, api_key, name, kind, nameservers):
        name = self.make_canonical(name)
        c_nameservers = []
        for ns in nameservers:
            ns = self.make_canonical(ns)
            c_nameservers.append(ns)
        print(c_nameservers)

        url = "http://{server_hostname}:8081/api/v1/servers/localhost/zones".format(
            server_hostname=server_hostname, zone=name)
        payload = {
            "name": name,
            "kind": kind,
            "masters": [],
            "records": [],
            "nameservers": c_nameservers,
            'comments': [{
                'name': name,
                'type': 'SOA',
                'account': '',
                'content': '',
            }],
        }
        headers = {'X-API-Key': api_key, 'Content-Type': 'application/json'}
        response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
        if response.status_code == 201:
            return response.json()
        elif response.status_code == 422:
            raise ValueError("The request was not formatted properly")
        else:
            error = "Something odd happened, response code was {code}".format(code=response.status_code)
            raise ValueError(error)

    def zone_delete(self, server_hostname, api_key, name):
        name = self.make_canonical(name)
        url = "http://{server_hostname}:8081/api/v1/servers/localhost/zones/{zone}".format(
            server_hostname=server_hostname, zone=name)
        headers = {'X-API-Key': api_key, 'Content-Type': 'application/json'}
        response = requests.request("DELETE", url, headers=headers)
        if response.status_code == 204:
            return "The zone was deleted successfully."
        elif response.status_code == 422:
              raise ValueError("The request was not formatted properly")
        else:
            error = "Something odd happened, response code was {code}".format(code=response.status_code)
            raise ValueError(error)

    def search_pdns(self, server_hostname, api_key, search_term, object_type, max_results):
        url = "http://{server_hostname}:8081/api/v1/servers/localhost/" \
              "search-data?q={q}&max={max}&object_type={object_type}".format(
            server_hostname=server_hostname, q=search_term, max=max_results, object_type=object_type)
        headers = {'X-API-Key': api_key}
        response = requests.request("GET", url, headers=headers)
        if response.status_code == 200:
            print(json.dumps(response.json(), indent=2))
        elif response.status_code == 422:
            raise ValueError("The request was not formatted properly")
        else:
            error = "Something odd happened, response code was {code}".format(code=response.status_code)
            raise ValueError(error)

    def make_canonical(self, name):
        if name[-1] != '.':
            return name + '.'

# CODE TO MANAGE POWERDNS RECORDS

    def record_create(self, server_hostname, api_key, zone, name, rtype, ttl, data, comments_content, comments_account):
        name = self.make_canonical(name)
        zone = self.make_canonical(zone)
        url = "http://{server_hostname}:8081/api/v1/servers/localhost/zones/{zone}".format(
            server_hostname=server_hostname, zone=zone)
        payload = {
            "rrsets": [{
                "name": name + zone,
                "type": rtype,
                "ttl": ttl,
                "changetype": "REPLACE",
                "records": [{
                    "content": data,
                    "disabled": False,
                }],
                "comments": [{
                    "account": comments_account,
                    "content": comments_content,
                }],
            }]
        }
        headers = {'X-API-Key': api_key, 'Content-Type': 'application/json'}
        response = requests.request("PATCH", url, headers=headers, data=json.dumps(payload))
        if response.status_code == 204:
            print("The Zone was created successfully.")
        elif response.status_code == 422:
            raise ValueError("The request was not formatted properly")
        else:
            error = "Something odd happened, response code was {code}".format(code=response.status_code)
            raise ValueError(error)

    def record_delete(self, server_hostname, api_key, zone, name, rtype):
        name = self.make_canonical(name)
        zone = self.make_canonical(zone)
        url = "http://{server_hostname}:8081/api/v1/servers/localhost/zones/{zone}".format(
            server_hostname=server_hostname, zone=zone)
        payload = {
            "rrsets": [{
                "name": name + zone,
                "type": rtype,
                "ttl": "",
                "changetype": "DELETE",
                "records": [{
                    "content": "",
                    "disabled": False,
                }],
                "comments": [{
                    "account": "",
                    "content": "",
                }],
            }]
        }
        headers = {'X-API-Key': api_key, 'Content-Type': 'application/json'}
        response = requests.request("PATCH", url, headers=headers, data=json.dumps(payload))
        if response.status_code == 204:
            print("The Zone was created successfully.")
        elif response.status_code == 422:
            raise ValueError("The request was not formatted properly")
        else:
            error = "Something odd happened, response code was {code}".format(code=response.status_code)
            raise ValueError(error)

    def record_update(self, server_hostname, api_key, zone, name, rtype, ttl, data, comments_content, comments_account):
        name = self.make_canonical(name)
        zone = self.make_canonical(zone)
        url = "http://{server_hostname}:8081/api/v1/servers/localhost/zones/{zone}".format(
            server_hostname=server_hostname, zone=zone)
        payload = {
            "rrsets": [{
                "name": name + zone,
                "type": rtype,
                "ttl": ttl,
                "changetype": "REPLACE",
                "records": [{
                    "content": data,
                    "disabled": False,
                }],
                "comments": [{
                    "account": comments_account,
                    "content": comments_content,
                }],
            }]
        }
        headers = {'X-API-Key': api_key, 'Content-Type': 'application/json'}
        response = requests.request("PATCH", url, headers=headers, data=json.dumps(payload))
        if response.status_code == 204:
            print("The Zone was updated successfully.")
        elif response.status_code == 422:
            raise ValueError("The request was not formatted properly")
        else:
            error = "Something odd happened, response code was {code}".format(code=response.status_code)
            raise ValueError(error)
