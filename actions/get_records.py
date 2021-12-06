from lib.base import PowerDNSClient


class Records(PowerDNSClient):
    def _run(self):
        return self.api.records
