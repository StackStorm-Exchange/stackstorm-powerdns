from lib.base import PowerDNSClient


class CreateZone(PowerDNSClient):
    def _run(self, *args, **kwargs):
        return self.api.create_zone(*args, **kwargs)
