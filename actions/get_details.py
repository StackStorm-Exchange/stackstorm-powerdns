from lib.base import PowerDNSClient


class Details(PowerDNSClient):
    def _run(self):
        return self.api.details
