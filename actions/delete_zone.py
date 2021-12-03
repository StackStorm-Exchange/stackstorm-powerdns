from lib.base import PowerDNSClient


class DeleteZone(PowerDNSClient):
    def _run(self, *args, **kwargs):
        return self.api.delete_zone(*args, **kwargs)
