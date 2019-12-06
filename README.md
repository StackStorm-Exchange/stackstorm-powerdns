# powerdns integration pack v0.0.1

> StackStorm intergratation for the PowerDNS API.
Carlos <nzlosh@yahoo.com>


## Configuration

The following options are required to be configured for the pack to work correctly.

| Option | Type | Required | Secret | Description |
|---|---|---|---|---|
| `api_key` | string | True | True | PowerDNS API Key |
| `api_url` | string | True | False | PowerDNS API. |


## Actions


The pack provides the following actions:

### servers_list
_Lists available PowerDNS servers_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `response_timeout` | number | False | default | _Time to wait for response to be received._ |
### zones_get
_Lists available zones_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `response_timeout` | number | False | default | _Time to wait for response to be received._ |
| `zone` | string | True | default | _The id of the server to retrieve_ |
### zones_list
_Lists available zones_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `response_timeout` | number | False | default | _Time to wait for response to be received._ |
| `server_id` | string | True | default | _The id of the server to retrieve_ |
### zone_create
_Create a new zone_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `name` | string | True | default | _Subject of the appointment._ |
| `nameservers` | array | True | default | _Date/time period to look for appointments._ |
| `kind` | string | True | default | _Native._ |
| `soa` | string | True | default | _Start of Authority_ |
| `rr_name` | string | True | default | _Resource record name_ |
| `rtype` | string | True | default | _Resource record type_ |
| `ttl` | string | True | default | _Time-To-Live for resource record_ |



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