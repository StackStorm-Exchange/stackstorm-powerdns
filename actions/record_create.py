from lib.base import PowerDNSClient


class RecordCreate(PowerDNSClient):
    """
    Create a new DNS Record.
    """
    def run(self, server_hostname, api_key, zone, name, rtype, ttl, data,
            comments_content, comments_account):
        record = self.record_create(server_hostname, api_key, zone, name, rtype, ttl, data, comments_content, comments_account)
        return record
