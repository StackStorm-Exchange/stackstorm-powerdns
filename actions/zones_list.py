from st2common.runners.base_action import Action
from lib.base import PowerDNSClient


class ZonesList(PowerDNSClient):
    """
    List zones.
    """
    def run(self, server, timeout=5):
        return (True, self.zones_list())
