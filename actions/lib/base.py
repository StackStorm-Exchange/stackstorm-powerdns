# coding=utf-8
from st2common import log as logging
from st2common.runners.base_action import Action
import powerdns


__all__ = ["PowerDNSClient"]

LOG = logging.getLogger(__name__)


class Record(object):
    """
    The RREntry object represents a single record.
    """

    def __init__(self, content, disabled=False):
        """
        content (string) - The content of this record
        disabled (boolean) - Whether or not this record is disabled. When unset, the
        record is not disabled
        set-ptr (boolean) - If set to true, the server will find the matching reverse zone
        and create a PTR there. Existing PTR records are replaced. If no matching reverse
        Zone, an error is thrown. Only valid in client bodies, only valid for A and AAAA types.
        Not returned by the server. This feature is deprecated and will be removed in 4.3.0.
        """
        self.content = content
        self.disabled = disabled
        self.set_ptr = False


class Comment(object):
    """
    A comment about an RRSet.
    """

    def __init__(self, content, account, modified_at):
        """
        Object Properties
        content (string) - The actual comment
        account (string) - Name of an account that added the comment
        modified_at (integer) - Timestamp of the last change to the comment
        """
        self.content = content
        self.account = account
        self.modified_at = modified_at


class RRSet(object):
    """
    This represents a Resource Record Set (all records with the same name and type).
    """

    def __init__(
        self, name, rec_type, ttl=86400, change_type="REPLACE", records=[], comments=[]
    ):
        """
        name (string) - Name for record set (e.g. "www.powerdns.com.")
        type (string) - Type of this record (e.g. "A", "PTR", "MX")
        ttl (integer) - DNS TTL of the records, in seconds. MUST NOT be included when
                        changetype is set to "DELETE".
        changetype (string) - MUST be added when updating the RRSet. Must be REPLACE or DELETE.
                              With DELETE, all existing RRs matching name and type will be
                              deleted, including all comments. With REPLACE: when records is present,
                              all existing RRs matching name and type will be deleted, and then new
                              records given in records will be created. If no records are left, any
                              existing comments will be deleted as well.  When comments is present,
                              all existing comments for the RRs matching name and type will be
                              deleted, and then new comments given in comments will be created. 
        records ([Record]) - All records in this RRSet. When updating Records, this is the list of new
                             records (replacing the old ones). Must be empty when changetype is set to
                             DELETE. An empty list results in deletion of all records (and comments).
        comments ([Comment]) - List of Comment. Must be empty when changetype is set to DELETE.
                               An empty list results in deletion of all comments.  modified_at is
                               optional and defaults to the current server time.
        """
        self.name = name
        self.rec_type = rec_type
        self.ttl = ttl
        self.change_type = change_type
        self.records = records
        self.comments = comments


class PowerDNSClient(Action):
    def __init__(self, config, timeout=5):
        super(PowerDNSClient, self).__init__(config)
        self.api_key = config.get("api_key")
        self.api_url = config.get("api_url")
        self.api_client = None
        self.api = None
        self.current_server = None
        self.current_zone = None

    def run(self, timeout):
        super(PowerDNSClient, self).run()
        self.api_client = powerdns.PDNSApiClient(
            api_endpoint=self.api_url, api_key=self.api_key, timeout=timeout
        )
        self.api = powerdns.PDNSEndpoint(self.api_client)

    def servers_list(self, string_list=True):
        server_list = []
        for server in self.api.servers:
            if string_list:
                server = str(server)
            server_list.append(server)
        return server_list

    def select_server(self, server_id):
        for server in self.servers_list(string_list=False):
            if str(server) == server_id:
                self.current_server = server
                break
        else:
            raise ValueError("Failed to find server {}".format(server))

    def select_zone(self, server_id, zone_name):
        self.select_server(server_id)
        self.current_zone = self.current_server.get_zone(zone_name)

    def zones_list(self, server_id):
        self.select_server(server_id)
        return [str(zone) for zone in self.current_server.zones]

    def zone_create(
        self,
        server_id,
        zone_name,
        kind,
        nameservers,
        masters=None,
        servers=None,
        rrsets=None,
        update=False,
    ):
        self.select_server(server_id)
        return self.current_server.create_zone(
            zone_name, kind, nameservers, masters, servers, rrsets, update
        )

    def zone_delete(self, server_id, zone_name):
        self.select_server(server_id)
        return self.current_server.delete_zone(zone_name)

    def zones_search(self, server_id, search_term, max_results):
        self.select_server(server_id)
        return self.current_server.search(search_term, max_results)

    def zone_details(self, server_id, zone_name):
        self.select_zone(server_id, zone_name)
        return self.current_zone.details

    def records_list(self, server_id, zone_name):
        self.select_zone(server_id, zone_name)
        return self.current_zone.records

    def record_get(self, server_id, zone_name, record_name):
        self.select_zone(server_id, zone_name)
        return self.current_zone.get_record(record_name)

    def records_create(self, server_id, zone_name, rrsets):
        self.select_zone(server_id, zone_name)
        return self.current_zone.create_records(rrsets)

    def records_delete(self, server_id, zone_name, rrsets):
        self.select_zone(server_id, zone_name)
        raise NotImplementedError
