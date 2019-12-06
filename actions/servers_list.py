from lib.base import PowerDNSClient


class ServerList(PowerDNSClient):
    """
    List available PowerDNS servers.
    """
    def run(self, timeout=5):
        return (True, self.servers_list())
