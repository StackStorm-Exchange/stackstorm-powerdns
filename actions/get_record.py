from lib.base import PowerDNSClient


class GetRecord(PowerDNSClient):
    def _run(self, *args, **kwargs):
        return self.api.get_record(*args, **kwargs)
