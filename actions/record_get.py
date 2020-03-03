from lib.base import PowerDNSClient


class RecordGet(PowerDNSClient):
    """
    Get record data.
    """

    def run(self, server_id, zone_name, record_name, response_timeout=5):
        super(RecordGet, self).run(response_timeout)
        return (True, self.record_get(server_id, zone_name, record_name))
