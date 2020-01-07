from lib.base import PowerDNSClient


class ServerList(PowerDNSClient):
    """
    List available PowerDNS servers.
    """

    def run(self, response_timeout):
        result = PowerDNSClient.servers_list(response_timeout)
        return result
