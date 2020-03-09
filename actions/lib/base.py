# coding=utf-8
from st2common import log as logging
from st2common.runners.base_action import Action
import powerdns


__all__ = ["PowerDNSClient"]

LOG = logging.getLogger(__name__)


class PowerDNSClientError(Exception):
    def __init__(self, message):
        self.message = message


class PowerDNSClient(Action):
    def __init__(self, config, timeout=5):
        super(PowerDNSClient, self).__init__(config)
        self.api_key = config.get("api_key")
        self.api_url = config.get("api_url")
        self.api_client = None
        self.api = None
        self.current_server = None
        self.current_zone = None

    def run(self, timeout):
        super(PowerDNSClient, self).run()
        self.api_client = powerdns.PDNSApiClient(
            api_endpoint=self.api_url, api_key=self.api_key, timeout=timeout
        )
        self.api = powerdns.PDNSEndpoint(self.api_client)

    def servers_list(self, string_list=True):
        server_list = []
        for server in self.api.servers:
            if string_list:
                server = str(server)
            server_list.append(server)
        return server_list

    def select_server(self, server_id):
        for server in self.servers_list(string_list=False):
            if str(server) == server_id:
                self.current_server = server
                break
        else:
            raise PowerDNSClientError("Failed to find server {}".format(server))

    def select_zone(self, server_id, zone_name):
        self.select_server(server_id)
        self.current_zone = self.current_server.get_zone(zone_name)
        if self.current_zone is None:
            raise PowerDNSClientError("Failed to find zone {}".format(zone_name))

    def zones_list(self, server_id):
        self.select_server(server_id)
        return [str(zone) for zone in self.current_server.zones]

    def zone_create(
        self,
        server_id,
        zone_name,
        kind,
        nameservers,
        masters=None,
        servers=None,
        rrsets=None,
        update=False,
    ):
        self.select_server(server_id)
        return self.current_server.create_zone(
            zone_name, kind, nameservers, masters, servers, rrsets, update
        )

    def zone_delete(self, server_id, zone_name):
        self.select_server(server_id)
        return self.current_server.delete_zone(zone_name)

    def zones_search(self, server_id, search_term, max_results):
        self.select_server(server_id)
        return self.current_server.search(search_term, max_results)

    def zone_details(self, server_id, zone_name):
        self.select_zone(server_id, zone_name)
        return self.current_zone.details

    def records_list(self, server_id, zone_name):
        self.select_zone(server_id, zone_name)
        return self.current_zone.records

    def record_get(self, server_id, zone_name, record_name):
        self.select_zone(server_id, zone_name)
        return self.current_zone.get_record(record_name)

    def records_create(self, server_id, zone_name, rrsets):
        self.select_zone(server_id, zone_name)
        return self.current_zone.create_records(rrsets)

    def records_delete(self, server_id, zone_name, rrsets):
        self.select_zone(server_id, zone_name)
        return self.current_zone.delete_records(rrsets)
