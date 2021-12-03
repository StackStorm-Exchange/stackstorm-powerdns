from lib.base import PowerDNSClient


class GetZone(PowerDNSClient):
    def _run(self, *args, **kwargs):
        return self.api.get_zone(*args, **kwargs)
