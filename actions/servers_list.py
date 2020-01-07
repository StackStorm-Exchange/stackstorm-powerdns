from lib.base import PowerDNSClient


#class ServerList(PowerDNSClient):
"""
List available PowerDNS servers.
"""
def run(self, response_timeout=5):
    client = PowerDNSClient()
    return True, client.servers_list()
