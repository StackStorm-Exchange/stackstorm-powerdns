from lib.base import PowerDNSClient


class SuggestZone(PowerDNSClient):
    def _run(self, *args, **kwargs):
        return self.api.suggest_zone(*args, **kwargs)
