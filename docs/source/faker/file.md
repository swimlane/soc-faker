# File

This documentation provides details about the data that can be faked for an File.

To retrieve generated/fake data for an File see the following capabilities:


```python
from socfaker import SocFaker

sc = SocFaker()

print(sc.file.name)
print(sc.file.extension)
print(sc.file.directory)
print(sc.file.drive_letter)
print(sc.file.gid)
print(sc.file.type)
print(sc.file.mime_type)
print(sc.file.size)
print(sc.file.timestamp)
print(sc.file.accessed_timestamp)
print(sc.file.attributes)
print(sc.file.version)
print(sc.file.build_version)
print(sc.file.checksum)
print(sc.file.install_scope)
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