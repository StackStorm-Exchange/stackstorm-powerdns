from lib.base import PowerDNSClient


class ZoneDetails(PowerDNSClient):
    """
    Get a zone details.
    """

    def run(self, server_id, zone_name, response_timeout=5):
        super(ZoneDetails, self).run(response_timeout)
        if not zone_name.endswith("."):
            return (False, "zone_name isn't canonical, it must end with a '.'")
        return (True, self.zone_details(server_id, zone_name))
