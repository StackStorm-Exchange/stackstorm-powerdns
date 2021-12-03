from lib.base import PowerDNSClient


class RestoreZone(PowerDNSClient):
    def _run(self, *args, **kwargs):
        return self.api.restore_zone(*args, **kwargs)
