from lib.base import PowerDNSClient


class RecordDelete(PowerDNSClient):
    """
    Delete a DNS Record.
    """
    def run(self, server_hostname, api_key, zone, name, rtype):
        record = self.record_delete(server_hostname, api_key, zone, name, rtype)
        return record
