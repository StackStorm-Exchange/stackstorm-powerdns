from lib.base import PowerDNSClient


class ZoneCreate(PowerDNSClient):
    """
    Create a new zone.
    """

    def run(
        self,
        server_id,
        zone_name,
        kind,
        nameservers,
        masters=None,
        servers=None,
        rrsets=None,
        update=False,
        response_timeout=5,
    ):
        super(ZoneCreate, self).run(response_timeout)
        return (
            True,
            self.zone_create(
                server_id, zone_name, kind, nameservers, masters, servers, rrsets, update,
            ),
        )
