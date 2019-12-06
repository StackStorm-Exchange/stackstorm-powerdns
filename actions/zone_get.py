from lib.base import PowerDNSClient


class GetZone(Action):
    """
    Get an existing zone.
    """
    def run(self, server_id, zone, response_timeout=5):
        client = PowerDNSClient(self.config, response_timeout)
        server = None
        for s in client.servers_list():
            if s.sid.endswith(server_id):
                server = s
                break
        if server is None:
            return (False, "No server found with name '{}'.".format(server_id))

        z = server.get_zone(zone)

        return (True, z)
