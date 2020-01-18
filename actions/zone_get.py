from lib.base import PowerDNSClient


class ZoneGet(PowerDNSClient):
    """
    Get a zone by name.
    """
    def run(self, name, server_hostname, api_key):
        zone = self.zone_get(server_hostname, api_key, name)
        return zone
