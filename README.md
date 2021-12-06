# powerdns integration pack v2.0.0

> StackStorm intergratation for the PowerDNS API. https://powerdns.com/
Carlos <nzlosh@yahoo.com>


## Configuration

The following options are required to be configured for the pack to work correctly.

| Option | Type | Required | Secret | Description |
|---|---|---|---|---|
| `api_key` | string | True | True | PowerDNS API Key |
| `api_url` | string | True | False | URL to PowerDNS API. |


## Actions


The pack provides the following actions:

### delete_records
_Delete resource record sets_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `rrset_comments` | array | True | default | _list of Comments instances for this RRSet_ |
| `rrset_ttl` | number | True | default | _Record time to live_ |
| `rrset_records` | array | True | default | _List of Str or Tuple(content_str, disabled_bool) or Dict with the keys “content” and optionally “disabled”._ |
| `rrset_rtype` | string | True | default | _Record type_ |
| `rrset_name` | string | True | default | _Record name_ |
| `rrset_changetype` | string | True | default | _API keyword DELETE or REPLACE_ |
| `response_timeout` | number | False | default | _Time to wait for a response from PowerDNS_ |
| `server_id` | string | True | default | _Server name to query._ |
| `zone_name` | string | True | default | _Zone's canonical name to get details._ |
### search
_Search term using API search endpoint_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `max_result` | number | False | default | __ |
| `search_term` | string | True | default | __ |
| `response_timeout` | number | False | default | _Time to wait for a response from PowerDNS_ |
| `server_id` | string | True | default | _Server name to query._ |
### suggest_zone
_Suggest best matching zone from existing zone_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `r_name` | string | True | default | _r_name_ |
| `response_timeout` | number | False | default | _Time to wait for a response from PowerDNS_ |
| `server_id` | string | True | default | _Server name to query._ |
### create_zone
_Create or update a (new) zone_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `rrset_comments` | array | True | default | _list of Comments instances for this RRSet_ |
| `rrset_ttl` | number | True | default | _Record time to live_ |
| `rrset_records` | array | True | default | _List of Str or Tuple(content_str, disabled_bool) or Dict with the keys “content” and optionally “disabled”._ |
| `rrset_rtype` | string | True | default | _Record type_ |
| `rrset_name` | string | True | default | _Record name_ |
| `rrset_changetype` | string | True | default | _API keyword DELETE or REPLACE_ |
| `response_timeout` | number | False | default | _Time to wait for a response from PowerDNS_ |
| `server_id` | string | True | default | _Server name to query._ |
| `update` | boolean | False | default | _If the zone need to be updated or created_ |
| `servers` | array | False | default | _List of forwarded-to servers (recursor only)_ |
| `masters` | array | False | default | _Zone masters_ |
| `nameservers` | array | True | default | _Name servers_ |
| `kind` | string | True | default | _Type of zone_ |
| `name` | string | True | default | _Name of zone_ |
### get_records
_Get zone’s records_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `zone_name` | string | True | default | _Zone's canonical name to get details._ |
| `response_timeout` | number | False | default | _Time to wait for a response from PowerDNS_ |
| `server_id` | string | True | default | _Server name to query._ |
### get_details
_Get zone’s detailed data_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `zone_name` | string | True | default | _Zone's canonical name to get details._ |
| `response_timeout` | number | False | default | _Time to wait for a response from PowerDNS_ |
| `server_id` | string | True | default | _Server name to query._ |
### notify
_Trigger notification for zone updates_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `zone_name` | string | True | default | _Zone's canonical name to get details._ |
| `response_timeout` | number | False | default | _Time to wait for a response from PowerDNS_ |
| `server_id` | string | True | default | _Server name to query._ |
### get_zones
_List of DNS zones on a PowerDNS server_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `response_timeout` | number | False | default | _Time to wait for a response from PowerDNS_ |
| `server_id` | string | True | default | _Server name to query._ |
### backup
_Backup zone data to json file_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `pretty_json` | boolean | False | default | _Enable pretty json display_ |
| `filename` | string | False | default | _Json file name_ |
| `directory` | string | True | default | _Directory to store json file_ |
| `zone_name` | string | True | default | _Zone's canonical name to get details._ |
| `response_timeout` | number | False | default | _Time to wait for a response from PowerDNS_ |
| `server_id` | string | True | default | _Server name to query._ |
### get_config
_Server configuration from PowerDNS API_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `response_timeout` | number | False | default | _Time to wait for a response from PowerDNS_ |
| `server_id` | string | True | default | _Server name to query._ |
### delete_zone
_Delete a zone_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `name` | string | True | default | _name_ |
| `response_timeout` | number | False | default | _Time to wait for a response from PowerDNS_ |
| `server_id` | string | True | default | _Server name to query._ |
### get_servers
_List PowerDNS servers_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `response_timeout` | number | False | default | _Time to wait for a response from PowerDNS_ |
| `server_id` | string | True | default | _Server name to query._ |
### create_records
_Create resource record sets_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `rrset_comments` | array | True | default | _list of Comments instances for this RRSet_ |
| `rrset_ttl` | number | True | default | _Record time to live_ |
| `rrset_records` | array | True | default | _List of Str or Tuple(content_str, disabled_bool) or Dict with the keys “content” and optionally “disabled”._ |
| `rrset_rtype` | string | True | default | _Record type_ |
| `rrset_name` | string | True | default | _Record name_ |
| `rrset_changetype` | string | True | default | _API keyword DELETE or REPLACE_ |
| `response_timeout` | number | False | default | _Time to wait for a response from PowerDNS_ |
| `server_id` | string | True | default | _Server name to query._ |
| `zone_name` | string | True | default | _Zone's canonical name to get details._ |
### restore_zone
_Restore a zone from a json file produced by PDNSZone.backup()_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `json_file` | string | True | default | _json_file_ |
| `response_timeout` | number | False | default | _Time to wait for a response from PowerDNS_ |
| `server_id` | string | True | default | _Server name to query._ |
### get_zone
_Get zone by name_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `name` | string | True | default | _name_ |
| `response_timeout` | number | False | default | _Time to wait for a response from PowerDNS_ |
| `server_id` | string | True | default | _Server name to query._ |
### get_record
_Get record data_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `name` | string | True | default | _name_ |
| `zone_name` | string | True | default | _Zone's canonical name to get details._ |
| `response_timeout` | number | False | default | _Time to wait for a response from PowerDNS_ |
| `server_id` | string | True | default | _Server name to query._ |



## Sensors

There are no sensors available for this pack.



## Authentication

 * To be advised.


## Limitations

 * Records can only be created or enitrely updated.  No partial record updates are currently supported.

## References

  * This pack uses [python-powerdns](https://github.com/outini/python-powerdns).


## Thanks to
  * Denis 'jawa' Pompilio for the python-powerdns project.
  * The PowerDNS project team.

<sub>Documentation generated using [pack2md](https://github.com/nzlosh/pack2md)</sub>