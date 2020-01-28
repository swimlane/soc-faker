# File

This documentation provides details about the data that can be faked for an File.

To retrieve generated/fake data for an File see the following capabilities:


```python
from socfaker import SocFaker

sc = SocFaker()

print(sc.file.filename)
print(sc.file.size)
print(sc.file.timestamp)
print(sc.file.hashes)
print(sc.file.md5)
print(sc.file.sha1)
print(sc.file.sha256)
print(sc.file.full_path)
print(sc.file.signed)
print(sc.file.signature)
print(sc.file.signature_status)
```

## File Class

```eval_rst
.. automodule:: socfaker.file
   :members:
   :undoc-members:
```