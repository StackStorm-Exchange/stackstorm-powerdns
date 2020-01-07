# coding=utf-8
from st2common import log as logging
from st2common.runners.base_action import Action
import powerdns


__all__ = [
    "PowerDNSClient"

]

LOG = logging.getLogger(__name__)


class PowerDNSClient(Action):

    def __init(self, config):
        super(PowerDNSClient, self).__init__(config)

    def setup_api(self):
        # primary function used to talk to powerdns library

        #setup api client
        api_client = powerdns.PDNSApiClient(api_endpoint=self.config['api_url'], api_key=self.config['api_key'])
        api = powerdns.PDNSEndpoint(api_client)
        return api



    # def __init__(self, config, timeout=5):
    #     super().__init__(config)
    #     self.api_key = config.get("api_key")
    #     self.api_url = config.get("api_url")
    #     self.api_client = None
    #     self.api = None
    #     self.current_server = None
    #     self.current_zone = None
    #
    # def run(self, timeout):
    #     super().run()
    #     self.api_client = powerdns.PDNSApiClient(
    #         api_endpoint=self.api_url,
    #         api_key=self.api_key,
    #         timeout=timeout
    #     )
    #     self.api = powerdns.PDNSEndpoint(self.api_client)
    #     return self.api
    #
    def servers_list(self):
        api = self.setup_api()
        server_list = api.servers
        return str(server for server in server_list)

    #
    # def select_server(self, server_id):
    #     for server in self.servers_list():
    #         if str(server) == server_id:
    #             self.current_server = server
    #             break
    #     else:
    #         raise ValueError("Failed to find server {}".format(server))
    #
    # def select_zone(self, name):
    #     self.current_zone = self.current_server.get_zone(name)
    #
##    def zones_list(self, server_id):
    #     self.select_server(server_id)
    #     return [str(zone) for zone in self.current_server.zones()]
    #
    # def zone_get(self, server_id, name):
    #     self.current_server = self.select_server(server_id)
    #     # return self.current_server.get_zone(name)
    #     return self.current_server.get_zone
    #
    #
    # def zone_create(
    #     self,
    #     server_id,
    #     name,
    #     kind,
    #     nameservers,
    #     masters=None,
    #     servers=None,
    #     rrsets=None,
    #     update=False
    # ):
    #     self.select_server(server_id)
    #     return self.current_server.create_zone(
    #         name,
    #         kind,
    #         nameservers,
    #         masters,
    #         servers,
    #         rrsets,
    #         update
    #     )
    #
    # def zone_delete(self, server_id, name):
    #     self.select_server(server_id)
    #     return self.current_server.delete_zone(name)
    #
    # def zones_search(self, server_id, search_term, max_results):
    #     self.select_server(server_id)
    #     return self.current_server.search(search_term, max_results)
    #
    # def zone_details(self, server_id, name):
    #     self.select_server(server_id)
    #     self.select_zone(name)
    #     self.current_zone.details()
