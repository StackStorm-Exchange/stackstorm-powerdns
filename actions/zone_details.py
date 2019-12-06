from lib.base import PowerDNSClient


class ZoneDetails(PowerDNSClient):
    """
    Get a zone details.
    """
    def run(self, server, name, timeout=5):
        super().run(timeout)
        return (True, self.zone_details(server, name))
