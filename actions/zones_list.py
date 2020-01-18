from lib.base import PowerDNSClient


class ZonesList(PowerDNSClient):
    """
    List zones.
    """
    def run(self, server_hostname, api_key):
        res = self.zones_list(server_hostname, api_key)
        return res
