# DNS

This documentation provides details about the data that can be faked for DNS information.

To retrieve generated/fake data for about DNS see the following capabilities:


```python
from socfaker import SocFaker

sc = SocFaker()

print(sc.dns.record)
print(sc.dns.header_flags)
print(sc.dns.id)
print(sc.dns.response_code)
print(sc.dns.op_code)
print(sc.dns.answers)
print(sc.dns.question)
print(sc.dns.direction)
print(sc.dns.name)
```

## DNS Class

```eval_rst
.. automodule:: socfaker.dns
   :members:
   :undoc-members:
```
