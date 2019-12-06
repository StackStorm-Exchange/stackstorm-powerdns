from st2common.runners.base_action import Action
from lib.base import PowerDNSClient


class ServerList(Action):
    """
    List all servers.
    """
    def run(self, server_id, response_timeout=5):
        client = PowerDNSClient(self.config, response_timeout)
        server = None
        for s in client.servers_list():
            if s.sid.endswith(server_id):
                server = s
                break
        if server is None:
            return (False, "No server found with name '{}'.".format(server_id))

        return (True, [str(z) for z in server.zones])
