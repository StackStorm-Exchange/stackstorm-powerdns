from lib.base import PowerDNSClient


class CreateRecords(PowerDNSClient):
    def _run(self, *args, **kwargs):
        return self.api.create_records(*args, **kwargs)
