from lib.base import PowerDNSClient, PowerDNSClientError


class RecordGet(PowerDNSClient):
    """
    Get record data.
    """

    def run(self, server_id, zone_name, record_name, response_timeout=5):
        super(RecordGet, self).run(response_timeout)
        try:
            return (True, self.record_get(server_id, zone_name, record_name))
        except PowerDNSClientError as e:
            return (False, "{}".format(e))
