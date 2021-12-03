from lib.base import PowerDNSClient


class Servers(PowerDNSClient):
    def _run(self):
        return self._api.servers
