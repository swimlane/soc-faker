# soc-faker

A python package for use in generating fake data for SOC and security automation.

## Install

To install you can create a virtual env or you can use the accompanying dockerfile to build/install this package.

To use the dockerfile run, cd to this repositories directory and run:

```
docker build --force-rm -t socfaker .
```

Once it is built, then run the docker container:

```
docker run socfaker
```

## Features

`socfaker` has many different ways to generate fake data.  Here are the basics for interacting with this package and properties:

```python
from socfaker import SocFaker

sc = SocFaker()

# Computer
print(sc.computer)
print(sc.computer.name)
print(sc.computer.disk)
print(sc.computer.memory)
print(sc.computer.platform)
print(sc.computer.mac_address)
print(sc.computer.os)

# Application
print(sc.application)
print(sc.application.status)
print(sc.application.account_status)
print(sc.application.name)
print(sc.application.logon_timestamp)

# Employee
print(sc.employee)
print(sc.employee.name)
print(sc.employee.first_name)
print(sc.employee.username)
print(sc.employee.email)
print(sc.employee.gender)
print(sc.employee.account_status)
print(sc.employee.ssn)
print(sc.employee.dob)
print(sc.employee.photo)
print(sc.employee.user_id)
print(sc.employee.phone_number)
print(sc.employee.logon_timestamp)
print(sc.employee.language)
print(sc.employee.title)
print(sc.employee.department)

# File
print(sc.file)
print(sc.file.filename)
print(sc.file.size)
print(sc.file.timestamp)
print(sc.file.hashes)
print(sc.file.md5)
print(sc.file.sha1)
print(sc.file.sha256)
print(sc.file.full_path())
print(sc.file.full_path(type='bin'))
print(sc.file.full_path(type='sys'))
print(sc.file.signed)
print(sc.file.signature)
print(sc.file.signature_status)

# Logs
print(sc.logs)
print(sc.logs.syslog())
print(sc.logs.windows)
print(sc.logs.windows.eventlog())
print(sc.logs.windows.sysmon())

# Network
print(sc.network)
print(sc.network.ipv4)
print(sc.network.ipv6)
print(sc.network.get_cidr_range('192.168.1.0/24'))
print(sc.network.hostname)
print(sc.network.netbios)
print(sc.network.mac)
print(sc.network.protocol)

# Organization
print(sc.organization)
print(sc.organization.name)
print(sc.organization.division)
print(sc.organization.title)

# Products
print(sc.products)

## Azure
print(sc.products.azure)
print(sc.products.azure.vm)
print(sc.products.azure.vm.details)
print(sc.products.azure.vm.metrics)
print(sc.products.azure.vm.metrics.average)
print(sc.products.azure.vm.metrics.graphs)
print(sc.products.azure.vm.topology)

## Elastic
print(sc.products.elastic)
print(sc.products.elastic.hits(count=1))

## QualysGuard
print(sc.products.qualysguard)
print(sc.products.qualysguard.scan(count=1))

## ServiceNow
print(sc.products.servicenow)
print(sc.products.servicenow.search())

# User Agent
print(sc.user_agent)

# Vulnerability
print(sc.vulnerability())
print(sc.vulnerability().host)
print(sc.vulnerability().scan)
print(sc.vulnerability().data)
print(sc.vulnerability().critical)
print(sc.vulnerability().high)
print(sc.vulnerability().medium)
print(sc.vulnerability().low)
print(sc.vulnerability().informational)

```


## TODO

### Employee

- [ ] Manager (Employee Object)

### Date
- [ ] Date Between
- [ ] Date X periods back (date after 1/1/2018)
- [ ] Date X per. Forward (date after 1/1/2018)
- [ ] Duration/Span

### Address
- [ ] Physical Address?

### Network
- [ ] URL


### File Info
- [ ] fuzzy?
- [ ] File Path
- [ ] File Reputation?

### PCAP

- [ ] Generate Fake PCAP files