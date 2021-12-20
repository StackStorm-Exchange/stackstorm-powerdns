from lib.base import PowerDNSClient


class Zones(PowerDNSClient):
    def _run(self):
        return [str(zone) for zone in self.api.zones]
