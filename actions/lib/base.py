# coding=utf-8
from st2common import log as logging
from st2common.runners.base_action import Action
import powerdns


__all__ = [
    "PowerDNSClient"
]

LOG = logging.getLogger(__name__)


class PowerDNSClient(Action):
    def __init__(self, config, timeout=5):
        super().__init__(config)
        self.api_key = config.api_key
        self.api_url = config.api_url
        self.api_client = None
        self.api = None
        self.current_server = None
        self.current_zone = None

    def run(self, timeout):
        super().run()
        self.api_client = powerdns.PDNSApiClient(
            api_endpoint=self.api_url,
            api_key=self.api_key,
            timeout=timeout
        )
        self.api = powerdns.PDNSEndpoint(self.api_client)

    def servers_list(self):
        return [str(server) for server in self.api.servers_list()]

    def select_server(self, server):
        for s in self.servers_list():
            if str(s) == server:
                self.current_server = s
                break
        else:
            raise ValueError("Failed to find server {}".format(server))

    def select_zone(self, name):
        self.current_zone = self.current_server.get_zone(name)

    def zones_list(self, server):
        self.select_server(server)
        return [str(zone) for zone in self.current_server.zones()]

    def zone_get(self, server, name):
        self.select_server(server)
        return self.current_server.get_zone(name)

    def zone_create(
        self,
        server,
        name,
        kind,
        nameservers,
        masters=None,
        servers=None,
        rrsets=None,
        update=False
    ):
        self.select_server(server)
        return self.current_server.create_zone(
            name,
            kind,
            nameservers,
            masters,
            servers,
            rrsets,
            update
        )

    def zone_delete(self, server, name):
        self.select_server(server)
        return self.current_server.delete_zone(name)

    def zones_search(self, server, search_term, max_results):
        self.select_server(server)
        return self.current_server.search(search_term, max_results)

    def zone_details(self, server, name):
        self.select_server(server)
        self.select_zone(name)
        self.current_zone.details()
