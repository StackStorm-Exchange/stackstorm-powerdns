from lib.base import PowerDNSClient, PowerDNSClientError
from powerdns import RRSet


class RecordsDelete(PowerDNSClient):
    """
    Delete resource record sets
    """

    def run(self, server_id, zone_name, record_name, record_type, response_timeout=5):
        super(RecordsDelete, self).run(response_timeout)
        try:
            rrsets = [RRSet(record_name, record_type, changetype="DELETE", records=[])]
            return (True, self.records_delete(server_id, zone_name, rrsets))
        except PowerDNSClientError as e:
            return (False, "{}".format(e))
