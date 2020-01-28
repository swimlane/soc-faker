# Network

This documentation provides details about the data that can be faked for Networks.

To retrieve generated/fake data for Networks see the following capabilities:


```python
from socfaker import SocFaker

sc = SocFaker()

print(sc.network.ipv4)
print(sc.network.ipv6)
print(sc.network.get_cidr_range('192.168.1.0/24'))
print(sc.network.hostname)
print(sc.network.netbios)
print(sc.network.mac)
print(sc.network.protocol)
```

## Network Class

```eval_rst
.. automodule:: socfaker.network
   :members:
   :undoc-members:
```