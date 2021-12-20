from lib.base import PowerDNSClient


class Servers(PowerDNSClient):
    def _run(self):
        return [str(server) for server in self._api.servers]
