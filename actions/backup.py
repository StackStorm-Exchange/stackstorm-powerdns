from lib.base import PowerDNSClient


class Backup(PowerDNSClient):
    def _run(self, *args, **kwargs):
        return self.api.backup(*args, **kwargs)
