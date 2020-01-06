from lib.base import PowerDNSClient


class ZoneGet(PowerDNSClient):
    """
    Get a zone by name.
    """
    def run(self, server_id, name, response_timeout=5):
        # call run from base.py and setup the api
        super().run(response_timeout)
        # call the function on return
        return (True, self.zone_get(server_id, name))
