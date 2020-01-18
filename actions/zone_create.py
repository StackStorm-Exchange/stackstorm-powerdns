from lib.base import PowerDNSClient


class ZoneCreate(PowerDNSClient):
    """
    Create a new zone.
    """
    def run(self, response_timeout, name, kind, nameservers, server_hostname, api_key):
        result = self.zone_create(server_hostname, api_key, name, kind, nameservers)
        return result
