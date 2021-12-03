from lib.base import PowerDNSClient


class Config(PowerDNSClient):
    def _run(self):
        return self.api.config
