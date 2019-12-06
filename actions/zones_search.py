from lib.base import PowerDNSClient


class ZonesSearch(PowerDNSClient):
    """
    Search for a term in all zones on the server.
    """
    def run(self, server, search_term, max_results=50, timeout=5):
        super().run(timeout)
        return (True, self.search(server, search_term, max_results))
