from lib.base import PowerDNSClient


class ServerList(PowerDNSClient):
    """
    List available PowerDNS servers.
    """

    def run(self,response_timeout):
        client = PowerDNSClient()
        result = client.servers_list()
        return result
