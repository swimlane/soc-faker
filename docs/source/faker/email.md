# Email

This documentation provides details about the data that can be faked for an Email.

To retrieve generated/fake data for an Employee see the following capabilities:


```python
from socfaker import SocFaker

sc = SocFaker()

print(sc.email.received_from)
print(sc.email.x_headers)
print(sc.email.date)
print(sc.email.to_address)
print(sc.email.from_address)
print(sc.email.subject)
print(sc.email.message_id)
print(sc.email.x_mailer)
print(sc.email.in_reply_to)
print(sc.email.body)
print(sc.email.email)
```

## Email Class

```eval_rst
.. automodule:: socfaker.email
   :members:
   :undoc-members:
```

