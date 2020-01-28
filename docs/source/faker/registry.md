# Alert

This documentation provides details about the data that can be faked for the Windows Registry.

To retrieve data about a fake Registry you can do the following:


```python
from socfaker import SocFaker

sc = SocFaker()

print(sc.registry.hive)
print(sc.registry.path)
```

## Alert Class

```eval_rst
.. automodule:: socfaker.registry
   :members:
   :undoc-members:
```