# Cloud

This documentation provides details about the data that can be faked for Cloud infrastructure.

To retrieve data about Cloud infrastructure you can do the following:


```python
from socfaker import SocFaker

sc = SocFaker()

print(sc.cloud.id)
print(sc.cloud.zone)
print(sc.cloud.instance_id)
print(sc.cloud.name)
print(sc.cloud.size)
print(sc.cloud.provider)
print(sc.cloud.region)
```

## Cloud Class

```eval_rst
.. automodule:: socfaker.cloud
   :members:
   :undoc-members:
```