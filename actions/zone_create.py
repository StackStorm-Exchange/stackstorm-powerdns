from lib.base import PowerDNSClient


class ZoneCreate(PowerDNSClient):
    """
    Create a new zone.
    """

    def run(self, server_id, name, nameservers, kind, soa, rr_name, rtype, ttl, response_timeout=5):
        super(ZoneCreate, self).run(response_timeout)
        return (
            True,
            self.zone_create(server_id, name, nameservers, kind, soa, rr_name, rtype, ttl),
        )
