from lib.base import PowerDNSClient


class DeleteRecords(PowerDNSClient):
    def _run(self, *args, **kwargs):
        return self.api.delete_records(*args, **kwargs)
