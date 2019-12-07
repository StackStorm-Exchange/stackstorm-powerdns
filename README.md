# powerdns integration pack v0.0.2

> StackStorm intergratation for the PowerDNS API.
Carlos <nzlosh@yahoo.com>


## Configuration

The following options are required to be configured for the pack to work correctly.

| Option | Type | Required | Secret | Description |
|---|---|---|---|---|
| `api_key` | string | True | True | PowerDNS API Key |
| `api_url` | string | True | False | URL to PowerDNS API. |


## Actions


The pack provides the following actions:

### zone_get
_Get a zone by name_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `name` | string | True | default | _Zone name to fetch._ |
| `server_id` | string | True | default | _Server name to query._ |
| `response_timeout` | integer | True | default | _Time to wait for a response from PowerDNS._ |
### zones_list
_Lists available zones_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `response_timeout` | number | False | default | _Time to wait for response to be received._ |
| `server_id` | string | True | default | _The id of the server to retrieve_ |
### zone_details
_Get zone details._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `name` | string | True | default | _Zone name to get details._ |
| `server_id` | string | True | default | _Server name to query._ |
| `response_timeout` | integer | True | default | _Time to wait for a response from PowerDNS._ |
### servers_list
_Lists available PowerDNS servers_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `response_timeout` | number | False | default | _Time to wait for response to be received._ |
### zones_search
_Search for terms in all zones on the server._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `search_term` | string | True | default | _The term to search for._ |
| `max_results` | string | True | default | _Limit the number of results returned in the search._ |
| `server_id` | string | True | default | _Server name to query._ |
| `response_timeout` | integer | True | default | _Time to wait for a response from PowerDNS._ |
### zone_delete
_Delete a zone by name_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `name` | string | True | default | _Zone name to delete._ |
| `server_id` | string | True | default | _Server name to query._ |
| `response_timeout` | integer | True | default | _Time to wait for a response from PowerDNS._ |
### zone_create
_Create a new zone_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `server_id` | string | default | default | _PowerDNS server to use_ |
| `response_timeout` | integer | default | default | _Time to wait for response from API._ |
| `name` | string | default | default | _Name of zone_ |
| `kind` | string | default | default | _Type of zone_ |
| `nameservers` | array | default | default | _Name servers_ |
| `masters` | array | default | default | _Zone masters_ |
| `servers` | array | default | default | _List of forwarded-to servers (recursor only)_ |
| `rrsets` | array | default | default | _Resource records sets_ |
| `update` | boolean | default | default | _If the zone need to be updated or created_ |



## Sensors

There are no sensors available for this pack.



## Authentication

 * To be advised.


## Limitations

 * To be advised.


## References

  * This pack uses [python-powerdns](https://github.com/outini/python-powerdns) under the hood.


## Thanks to

<sub>Documentation generated using [pack2md](https://github.com/nzlosh/pack2md)</sub>