from lib.base import PowerDNSClient


class RecordsDelete(PowerDNSClient):
    """
    Delete resource record sets
    """

    def run(self, server_id, zone_name, rrsets, response_timeout=5):
        super(RecordsDelete, self).run(response_timeout)
        return (True, self.records_delete(server_id, zone_name, rrsets))
