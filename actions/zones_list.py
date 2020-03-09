from lib.base import PowerDNSClient


class ZonesList(PowerDNSClient):
    """
    List zones.
    """

    def run(self, server_id, response_timeout=5):
        super(ZonesList, self).run(response_timeout)
        return (True, self.zones_list(server_id))
