from lib.base import PowerDNSClient


class ZoneGet(PowerDNSClient):
    """
    Get a zone by name.
    """
    def run(self, server, name, timeout=5):
        super().run(timeout)
        return (True, self.zone_get(server, name))