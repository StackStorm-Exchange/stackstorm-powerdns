from lib.base import PowerDNSClient, PowerDNSClientError


class ZoneDelete(PowerDNSClient):
    """
    Delete a zone by name.
    """

    def run(self, server_id, zone_name, response_timeout=5):
        super(ZoneDelete, self).run(response_timeout)
        try:
            return (True, self.zone_delete(server_id, zone_name))
        except PowerDNSClientError as e:
            return (False, "{}".format(e))
