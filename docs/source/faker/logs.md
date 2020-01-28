# File

This documentation provides details about the data that can be faked for Logs.

To retrieve generated/fake data for Logs see the following capabilities:


```python
from socfaker import SocFaker

sc = SocFaker()

print(sc.logs.syslog())
print(sc.logs.windows)
print(sc.logs.windows.eventlog())
print(sc.logs.windows.sysmon())
```

## SysLog Class

```eval_rst
.. automodule:: socfaker.logstreamer
   :members:
   :undoc-members:
```

## Windows Event Log Class

```eval_rst
.. automodule:: socfaker.windowseventlog
   :members:
   :undoc-members:
```

## Windows Symon Log Class

```eval_rst
.. automodule:: socfaker.sysmon
   :members:
   :undoc-members:
```