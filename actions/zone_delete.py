from lib.base import PowerDNSClient


class ZoneDelete(PowerDNSClient):
    """
    Delete a zone by name.
    """
    def run(self, server, name, timeout=5):
        super().run(timeout)
        return (True, self.zone_delete(name))
