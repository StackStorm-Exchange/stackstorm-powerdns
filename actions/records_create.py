from lib.base import PowerDNSClient
from powerdns import RRSet


class RecordsCreate(PowerDNSClient):
    """
    Create resource record sets.
    """

    def run(
        self,
        server_id,
        zone_name,
        record_name,
        record_type,
        record_ttl,
        change_type,
        records=[],
        response_timeout=5,
    ):
        super(RecordsCreate, self).run(response_timeout)
        rrsets = [
            RRSet(
                name=record_name,
                rtype=record_type,
                records=records,
                ttl=record_ttl,
                changetype=change_type,
            )
        ]
        return (True, self.records_create(server_id, zone_name, rrsets))
