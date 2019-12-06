from st2common.runners.base_action import Action
from lib.base import PowerDNSClient


class ServerList(Action):
    """
    List all servers.
    """
    def run(self, response_timeout=5):
        client = PowerDNSClient(self.config, response_timeout)
        return (True, [str(s) for s in client.servers_list()])
