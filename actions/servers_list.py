from lib.base import PowerDNSClient


class ServerList(PowerDNSClient):
    """
    List available PowerDNS servers.
    """
    def run(self, response_timeout=5):
        super(ServerList, self).run(response_timeout)
        return (True, self.servers_list())
