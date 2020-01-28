# Alert

This documentation provides details about the data that can be faked for an Alert.

To retrieve data about a fake Alert you can do the following:


```python
from socfaker import SocFaker

sc = SocFaker()

print(sc.alert.summary)
print(sc.alert.signature_name)
print(sc.alert.type)
print(sc.alert.status)
print(sc.alert.action)
print(sc.alert.direction)
print(sc.alert.location)
```

## Alert Class

```eval_rst
.. automodule:: socfaker.alert
   :members:
   :undoc-members:
```