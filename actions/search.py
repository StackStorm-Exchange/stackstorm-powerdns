from lib.base import PowerDNSClient


class Search(PowerDNSClient):
    def _run(self, *args, **kwargs):
        return self.api.search(*args, **kwargs)
