# Elastic

This documentation provides details about the data that can be faked for Elastic.

To retrieve generated/fake data for Elastic see the following capabilities:


```python
from socfaker import SocFaker

sc = SocFaker()

print(sc.products.elastic)
print(sc.products.elastic.hits(count=1))
```

## Elastic Class

```eval_rst
.. automodule:: socfaker.elastichits
   :members:
   :undoc-members:
```


