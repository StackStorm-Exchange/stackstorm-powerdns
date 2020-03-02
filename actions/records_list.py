from lib.base import PowerDNSClient


class RecordsList(PowerDNSClient):
    """
    List records.
    """

    def run(self, server_id, zone_name, response_timeout=5):
        super(RecordsList, self).run(response_timeout)
        return (True, self.records_list(server_id, zone_name))
