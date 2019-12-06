# coding=utf-8
from st2common import log as logging
import powerdns

__all__ = [
    "PowerDNSClient"
]

LOG = logging.getLogger(__name__)


class PowerDNSClient(object):
    def __init__(self, config, timeout=5):
        api_key = config.get("api_key", "")
        api_url = config.get("api_url", "http://localhost:8081/api/v1")
        self.api = powerdns.PDNSEndpoint(
            powerdns.PDNSApiClient(
                api_endpoint=api_url,
                api_key=api_key,
                timeout=timeout
            )
        )

    def servers_list(self):
        """
        List all servers.
        """
        return self.api.servers

    def server_get(self, server_id):
        """
        List a server
        server_id (string) - The id of the server to retrieve.
        """
        route = f"/servers/{server_id}"
        verb = "GET"

    def zones_list(self, server_id, zone=None):
        """
        List all Zones in a server
        server_id (string) – The id of the server to retrieve.
        zone (string) – When set to the name of a zone, only this zone is returned. If no
                        zone with that name exists, the response is an empty array. This can
                        e.g. be used to check if a zone exists in the database without having to
                        guess/encode the zone’s id or to check if a zone exists.
        """
        route = f"/servers/{server_id}/zones"
        verb = "GET"
        if zone:
            query_string = f"zone={zone}"
        else:
            query_string = ""

    def zone_create(self, server_id, rrsets=True):
        """
        Creates a new domain, returns the Zone on creation.
        server_id (string) – The id of the server to retrieve
        rrsets (boolean) – "true" (default) or "false", whether to include the "rrsets" in the
                           response Zone object.
        """
        route = f"/servers/{server_id}/zones"
        verb = "POST"
        if rrsets:
            query_string = f"rrsets=f{str(rrsets).lower()}"
        else:
            query_string = ""

    def zone_get(self, server_id, zone_id):
        """
        Get zone managed by a server.
        server_id (string) – The id of the server to retrieve
        zone_id (string) – The id of the zone to retrieve
        """
        self.route = f"/servers/{server_id}/zones/{zone_id}"
        verb = "GET"

    def zone_delete(self, server_id, zone_id):
        """
        Deletes this zone, all attached metadata and rrsets.
        server_id (string) – The id of the server to retrieve
        zone_id (string) – The id of the zone to retrieve
        """
        self.route = f"/servers/{server_id}/zones/{zone_id}"
        verb = "DELETE"

    def zone_cud(self, server_id, zone_id):
        """
        Creates/modifies/deletes RRsets present in the payload and their comments.
        Returns 204 No Content on success.
        server_id (string) – The id of the server to retrieve
        zone_id (string) –
        """
        route = f"/servers/{server_id}/zones/{zone_id}"
        verb = "PATCH"

    def zone_modify_metadata(self, server_id, zone_id):
        """
        Modifies basic zone data (metadata).
        Allowed fields in client body: all except id, url and name.
        server_id (string) – The id of the server to retrieve
        zone_id (string) –
        """
        route = f"/servers/{server_id}/zones/{zone_id}"
        verb = "PUT"

    def zone_axfr_retrieve(self, server_id, zone_id):
        """
        Retrieve slave zone from its master.
        Fails when zone kind is not Slave, or slave is disabled in the configuration.
        Clients MUST NOT send a body.
        server_id (string) – The id of the server to retrieve
        zone_id (string) – The id of the zone to retrieve
        """
        route = f"/servers/{server_id}/zones/{zone_id}/axfr-retrieve"
        verb = "PUT"

    def zone_notify_slaves(self, server_id, zone_id):
        """
        Send a DNS NOTIFY to all slaves.
        Fails when zone kind is not Master or Slave, or master and slave are disabled
        in the configuration. Only works for Slave if renotify is on. Clients MUST NOT send a body.
        server_id (string) – The id of the server to retrieve
        zone_id (string) – The id of the zone to retrieve
        """

        route = f"/servers/{server_id}/zones/{zone_id}/notify"
        verb = "PUT"

    def zone_get_axfr_format(self, server_id, zone_id):
        """
        Returns the zone in AXFR format.
        server_id (string) – The id of the server to retrieve
        zone_id (string) – The id of the zone to retrieve
        """
        route = f"/servers/{server_id}/zones/{zone_id}/export"
        verb = "GET"

    def zone_check(self, server_id, zone_id):
        """
        Verify zone contents/configuration.
        server_id (string) – The id of the server to retrieve
        zone_id (string) – The id of the zone to retrieve
        """
        route = f"/servers/{server_id}/zones/{zone_id}/check"
        verb = "GET"

    def zone_rectify(self, server_id, zone_id):
        """
        Rectify the zone data.
        This does not take into account the API-RECTIFY metadata. Fails on slave zones and
        zones that do not have DNSSEC.
        server_id (string) – The id of the server to retrieve
        zone_id (string) – The id of the zone to retrieve
        """
        route = f"/servers/{server_id}/zones/{zone_id}/rectify"
        verb = "PUT"

    def cryptkeys_get(self, server_id, zone_id):
        """
        Get all CryptoKeys for a zone, except the privatekey
        Parameters
        • server_id (string) – The id of the server to retrieve
        • zone_id (string) – The id of the zone to retrieve
        """
        route = f"/servers/{server_id}/zones/{zone_id}/cryptokeys"
        verb = "GET"

    def cryptkeys_create(self, server_id, zone_id):
        """
        Creates a Cryptokey
        This method adds a new key to a zone. The key can either be generated or imported by
        supplying the content parameter. if content, bits and algo are null, a key will be
        generated based on the default-ksk-algorithm and default-ksk-size settings for a KSK and
        the default-zsk-algorithm and default-zsk-size options for a ZSK.
        server_id (string) – The id of the server to retrieve
        zone_id (string) –
        """
        route = f"/servers/{server_id}/zones/{zone_id}/cryptokeys"
        verb = "POST"

    def cryptkey_get(self, server_id, zone_id, cryptkey_id):
        """
        Returns all data about the CryptoKey, including the privatekey.
        server_id (string) – The id of the server to retrieve
        zone_id (string) – The id of the zone to retrieve
        cryptokey_id (string) – The id value of the CryptoKey
        """
        route = f"/servers/{server_id}/zones/{zone_id}/cryptokeys/{cryptokey_id}"
        verb = "GET"

    def cryptkey_activation_toggle(server_id, zone_id, cryptkey_id):
        """
        This method (de)activates a key from zone_name specified by cryptokey_id
        server_id (string) – The id of the server to retrieve
        zone_id (string) –
        cryptokey_id (string) – Cryptokey to manipulate
        """
        route = f"/servers/{server_id}/zones/{zone_id}/cryptokeys/{cryptokey_id}"
        verb = "PUT"

    def cryptkey_delete(self, server_id, zone_id, cryptokey_id):
        """
        This method deletes a key specified by cryptokey_id.
        Parameters
        • server_id (string) – The id of the server to retrieve
        • zone_id (string) – The id of the zone to retrieve
        • cryptokey_id (string) – The id value of the Cryptokey
        """
        verb = "DELETE"
        route = f"/servers/{server_id}/zones/{zone_id}/cryptokeys/{cryptokey_id}"

    def metadata_get(self, server_id, zone_id):
        """
        Get all the MetaData associated with the zone.
        server_id (string) – The id of the server to retrieve
        zone_id (string) – The id of the zone to retrieve
        """
        verb = "GET"
        route = f"/servers/{server_id}/zones/{zone_id}/metadata"

    def metadata_create(self, server_id, zone_id):
        """
        Creates a set of metadata entries
        Creates a set of metadata entries of given kind for the zone.
        Existing metadata entries for the zone with the same kind are not overwritten.
        server_id (string) – The id of the server to retrieve
        zone_id (string) –
        """
        verb = "POST"
        route = f"/servers/{server_id}/zones/{zone_id}/metadata"

    def metadata_list_by_kind(server_id, zone_id, metadata_kind):
        """
        Get the content of a single kind of domain metadata as a list of MetaData objects.
        server_id (string) – The id of the server to retrieve
        zone_id (string) – The id of the zone to retrieve
        metadata_kind (string) – ???
        """
        route = f"/servers/{server_id}/zones/{zone_id}/metadata/{metadata_kind}"
        verb = "GET"

    def metadata_modify_by_kind(self, server_id, zone_id, metadata_kind):
        """
        Modify the content of a single kind of domain metadata.
        server_id (string) – The id of the server to retrieve
        zone_id (string) –
        metadata_kind (string) – The kind of metadata
        """
        verb = "PUT"
        route = f"/servers/{server_id}/zones/{zone_id}/metadata/{metadata_kind}"

    def metadata_delete_kind(self, server_id, zone_id, metadata_kind):
        """
        Delete all items of a single kind of domain metadata.
        server_id (string) – The id of the server to retrieve
        zone_id (string) – The id of the zone to retrieve
        metadata_kind (string) – ???
        """
        verb = "DELETE"
        route = f"/servers/{server_id}/zones/{zone_id}/metadata/{metadata_kind}"

    def metadata_search(self, server_id, search_string, max_entries):
        """
        Search the data inside PowerDNS
        Search the data inside PowerDNS for search_term and return at most max_results. This
        includes zones, records and comments. The * character can be used in search_term as a
        wildcard character and the ? character can be used as a wildcard for a single character.
        server_id (string) – The id of the server to retrieve
        q (string) – The string to search for
        max (integer) – Maximum number of entries to return
        """
        verb = "GET"
        route = f"/servers/{server_id}/search-data"
        query = {}
        if search_string:
            query["q"] = search_string
        if max_entries:
            query["max"] = max_entries

    def statistics_query(self, server_id):
        """
        Query statistics.
        Query PowerDNS internal statistics. Returns a list of BaseStatisticItem derived elements.
        server_id (string) – The id of the server to retrieve
        """
        verb = "GET"
        route = f"/servers/{server_id}/statistics"

    def cache_flush(self, server_id, domain=None):
        """
        Flush a cache-entry by name
        Parameters
        • server_id (string) – The id of the server to retrieve
        Query Parameters
        • domain (string) – The domain name to flush from the cache
        """
        verb = "PUT"
        route = f"/servers/{server_id}/cache/flush"
        query = {}
        if domain:
            query["domain"] = domain
