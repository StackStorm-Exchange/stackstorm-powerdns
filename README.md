# powerdns integration pack v1.4.0

> StackStorm integration for the PowerDNS API.
KenV <kvedder@amplex.net>


## Configuration

The following options are required to be configured for the pack to work correctly.

| Option | Type | Required | Secret | Description |
|---|---|---|---|---|
None


## Actions


The pack provides the following actions:

### zone_create
_Create a new zone_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `server_hostname` | string | True | default | _Hostname of the server_ |
| `api_key` | string | True | default | _API Key for Server_ |
| `name` | string | True | default | _Name of zone_ |
| `kind` | string | True | default | _Type of zone. (Native, Master, or Slave)_ |
| `nameservers` | array | True | default | _list of nameservers to use_ |
### record_create
_Create a new record inside a zone._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `server_hostname` | string | True | default | _Server Hostname To Query_ |
| `api_key` | string | True | default | _API Key for Server_ |
| `zone` | string | True | default | _Name of zone to add the record to. (Must be canonical with period at the end.)_ |
| `name` | string | True | default | _Name of the record_ |
| `rtype` | string | True | default | _Type of record._ |
| `ttl` | integer | True | default | _Time to live (in seconds)._ |
| `data` | string | True | default | _The data portion of the record._ |
| `comments_content` | string | default | default | _Comments.Content Field for the Record_ |
| `comments_account` | string | default | default | _Comments.account Field for the Record_ |
### zones_list
_Lists available zones_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `server_hostname` | string | True | default | _Server Hostname To Query_ |
| `api_key` | string | True | default | _API Key for Server_ |
### zone_get
_Get a zone's details by name_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `name` | string | True | default | _Zone name to fetch. (must be canonical and end in a period.)_ |
| `server_hostname` | string | True | default | _Server Hostname To Query_ |
| `api_key` | string | True | default | _API Key for Server_ |
| `response_timeout` | integer | True | default | _Time to wait for a response from PowerDNS._ |
### record_delete
_Delete a new record inside a zone._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `server_hostname` | string | True | default | _Server Hostname To Query_ |
| `api_key` | string | True | default | _API Key for Server_ |
| `zone` | string | True | default | _Name of zone to delete the record from. (Must be canonical with period at the end.)_ |
| `name` | string | True | default | _Name of the record_ |
| `rtype` | string | True | default | _Type of record._ |
### search_pdns
_Search PowerDNS for matching items in both records and zones._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `search_term` | string | True | default | _Term to search for. Wildcard * is allowed. Example: *searchterm*_ |
| `server_hostname` | string | True | default | _Server Hostname To Query_ |
| `object_type` | string | True | default | _the object type to search for_ |
| `api_key` | string | True | default | _API Key for Server_ |
| `max_results` | integer | True | default | _Maximum Number of Results_ |
### zone_delete
_Delete a zone by name_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `name` | string | True | default | _Zone name to delete._ |
| `server_hostname` | string | True | default | _Hostname of the server_ |
| `api_key` | string | True | default | _API Key for Server_ |
### record_update
_Create a new record inside a zone._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `server_hostname` | string | True | default | _Server Hostname To Query_ |
| `api_key` | string | True | default | _API Key for Server_ |
| `zone` | string | True | default | _Name of zone to update the record in. (Must be canonical with period at the end.)_ |
| `name` | string | True | default | _Name of the record. (must already exist)_ |
| `rtype` | string | True | default | _Type of record._ |
| `ttl` | integer | True | default | _Time to live (in seconds)._ |
| `data` | string | True | default | _The data portion of the record._ |
| `comments_content` | string | default | default | _Comments.Content Field for the Record_ |
| `comments_account` | string | default | default | _Comments.account Field for the Record_ |



## Sensors

There are no sensors available for this pack.



## Authentication

 * To be advised.


## Limitations

 * To be advised.


## References

  * This pack uses [python-powerdns](https://github.com/outini/python-powerdns) under the hood.


## Thanks to

<sub>Documentation generated using [pack2md](https://github.com/nzlosh/pack2md)