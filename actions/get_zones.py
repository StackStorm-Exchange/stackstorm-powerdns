from lib.base import PowerDNSClient


class Zones(PowerDNSClient):
    def _run(self):
        return self.api.zones
