from lib.base import PowerDNSClient


class ZoneCreate(PowerDNSClient):
    """
    Create a new zone.
    """
    def run(
        self,
        server,
        name,
        nameservers,
        kind,
        soa,
        rr_name,
        rtype,
        ttl,
        timeout=5
    ):
        super().run(timeout)
        return (
            True,
            self.zone_create(
                server,
                name,
                nameservers,
                kind,
                soa,
                rr_name,
                rtype,
                ttl
            )
        )
