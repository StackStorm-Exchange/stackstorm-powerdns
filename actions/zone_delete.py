from lib.base import PowerDNSClient


class ZoneDelete(PowerDNSClient):
    """
    Delete a zone by name.
    """
    def run(self, server_hostname, api_key, name):
        deleted = self.zone_delete(server_hostname, api_key, name)
        return deleted
