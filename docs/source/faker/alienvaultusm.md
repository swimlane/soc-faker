# AlienVault USM

This documentation provides details about the data that can be faked for AlienVault USM.

To retrieve generated/fake data for AlienVault USM see the following capabilities:


```python
from socfaker import SocFaker

sc = SocFaker()

print(sc.products.alienvault.USM.event_type)
print(sc.products.alienvault.USM.id)
print(sc.products.alienvault.USM.description)
print(sc.products.alienvault.USM.severity)
print(sc.products.alienvault.USM.action)
print(sc.products.alienvault.USM.category)
print(sc.products.alienvault.USM.subcategory)
print(sc.products.alienvault.USM.destination_hostname)
print(sc.products.alienvault.USM.destination_fqdn)
print(sc.products.alienvault.USM.destination_address)
print(sc.products.alienvault.USM.destination_port)
print(sc.products.alienvault.USM.destination_port_label)
print(sc.products.alienvault.USM.destination_asset_id)
print(sc.products.alienvault.USM.destination_longitude)
print(sc.products.alienvault.USM.destination_latitude)
print(sc.products.alienvault.USM.destination_city)
print(sc.products.alienvault.USM.destination_country)
print(sc.products.alienvault.USM.destination_region)
print(sc.products.alienvault.USM.source_hostname)
print(sc.products.alienvault.USM.source_fqdn)
print(sc.products.alienvault.USM.source_address)
print(sc.products.alienvault.USM.source_port)
print(sc.products.alienvault.USM.source_port_label)
print(sc.products.alienvault.USM.source_asset_id)
print(sc.products.alienvault.USM.source_longitude)
print(sc.products.alienvault.USM.source_latitude)
print(sc.products.alienvault.USM.source_city)
print(sc.products.alienvault.USM.source_country)
print(sc.products.alienvault.USM.source_region)
print(sc.products.alienvault.USM.plugin)
print(sc.products.alienvault.USM.plugin_device)
print(sc.products.alienvault.USM.plugin_device_type)
print(sc.products.alienvault.USM.plugin_version)
print(sc.products.alienvault.USM.packets_sent)
print(sc.products.alienvault.USM.packets_received)
print(sc.products.alienvault.USM.packet_type)
print(sc.products.alienvault.USM.bytes_in)
print(sc.products.alienvault.USM.bytes_out)
print(sc.products.alienvault.USM.app_display_name)
print(sc.products.alienvault.USM.application_protocol)
print(sc.products.alienvault.USM.transport_protocol)
```

## AlienVault USM Class

```eval_rst
.. automodule:: socfaker.alienvaultusm
   :members:
   :undoc-members:
```