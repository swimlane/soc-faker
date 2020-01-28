# Azure

This documentation provides details about the data that can be faked for Microsoft Azure.

To retrieve generated/fake data for Microsoft Azure see the following capabilities:


```python
from socfaker import SocFaker

sc = SocFaker()

print(sc.products.azure.vm)
print(sc.products.azure.vm.details)
print(sc.products.azure.vm.metrics)
print(sc.products.azure.vm.metrics.average)
print(sc.products.azure.vm.metrics.graphs)
print(sc.products.azure.vm.topology)
```

## Azure VM Class

```eval_rst
.. automodule:: socfaker.azurevm
   :members:
   :undoc-members:
```

## Azure VM Metrics Class

```eval_rst
.. automodule:: socfaker.azurevmmetrics
   :members:
   :undoc-members:
```

## Azure VM Topology Class

```eval_rst
.. automodule:: socfaker.azurevmtopology
   :members:
   :undoc-members:
```