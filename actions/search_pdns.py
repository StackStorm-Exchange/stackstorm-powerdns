from lib.base import PowerDNSClient


class SearchPDNS(PowerDNSClient):
    """
    Delete a zone by name.
    """
    def run(self, server_hostname, api_key, search_term, max_results, object_type):
        result = self.search_pdns(server_hostname, api_key, search_term, object_type,max_results)
        return result
