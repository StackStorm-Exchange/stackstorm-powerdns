from lib.base import PowerDNSClient


class ZoneDetails(PowerDNSClient):
    """
    Get a zone details.
    """
    def run(self, server_id, name, response_timeout=5):
        super().run(response_timeout)
        return (True, self.zone_details(server_id, name))
