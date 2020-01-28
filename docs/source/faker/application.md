# Application

This documentation provides details about the data that can be faked for an application.

To retrieve data about a fake application you can do the following:


```python
from socfaker import SocFaker

sc = SocFaker()

print(sc.application)
print(sc.application.status)
print(sc.application.account_status)
print(sc.application.name)
print(sc.application.logon_timestamp)
```

## Application Class

```eval_rst
.. automodule:: socfaker.application
   :members:
   :undoc-members:
```