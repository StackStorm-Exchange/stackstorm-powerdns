from lib.base import PowerDNSClient


class RecordsCreate(PowerDNSClient):
    """
    Create resource record sets.
    """

    def run(self, server_id, zone_name, rrsets, response_timeout=5):
        super(RecordsCreate, self).run(response_timeout)
        return (True, self.records_create(server_id, zone_name, rrsets))
