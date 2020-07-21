# Process

This documentation provides details about the data that can be faked for Processes.

To retrieve generated/fake data for processes see the following capabilities:


```python
from socfaker import SocFaker

sc = SocFaker()

print(sc.process.args)
print(sc.process.args_count)
print(sc.process.command_line)
print(sc.process.entity_id)
print(sc.process.executable)
print(sc.process.name)
print(sc.process.parent)
print(sc.process.pid)
print(sc.process.start)
print(sc.process.thread_id)
```

## Process Class

```eval_rst
.. automodule:: socfaker.process
   :members:
   :undoc-members:
```