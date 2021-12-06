from lib.base import PowerDNSClient


class Notify(PowerDNSClient):
    def _run(self, *args, **kwargs):
        return self.api.notify(*args, **kwargs)
