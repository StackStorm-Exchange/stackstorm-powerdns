from lib.base import PowerDNSClient


class ZoneGet(PowerDNSClient):
    """
    Get a zone by name.
    """
    def run(self, server_id, name, response_timeout=5):
        super(ZoneGet, self).run(response_timeout)
        return (True, self.zone_get(server_id, name))
