# Agent

This documentation provides details about the data that can be faked for an Agent.

To retrieve data about a fake Agent you can do the following:


```python
from socfaker import SocFaker

sc = SocFaker()

print(sc.agent.ephermeral_id)
print(sc.agent.id)
print(sc.agent.type)
print(sc.agent.name)
print(sc.agent.version)
```

## Agent Class

```eval_rst
.. automodule:: socfaker.agent
   :members:
   :undoc-members:
```