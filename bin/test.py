from socfaker import SocFaker

sc = SocFaker(github_token='YOUR GITHUB TOKEN')

# Alert
print(sc.alert.summary)
print(sc.alert.signature_name)
print(sc.alert.type)
print(sc.alert.status)
print(sc.alert.action)
print(sc.alert.direction)
print(sc.alert.location)

# Computer
print(sc.computer.name)
print(sc.computer.disk)
print(sc.computer.memory)
print(sc.computer.platform)
print(sc.computer.mac_address)
print(sc.computer.os)

# Application
print(sc.application.status)
print(sc.application.account_status)
print(sc.application.name)
print(sc.application.logon_timestamp)

# Employee
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

# Logs
print(sc.logs.syslog())
print(sc.logs.windows)
print(sc.logs.windows.eventlog())
print(sc.logs.windows.sysmon())

# Network
print(sc.network.ipv4)
print(sc.network.ipv6)
print(sc.network.get_cidr_range('192.168.1.0/24'))
print(sc.network.hostname)
print(sc.network.netbios)
print(sc.network.mac)
print(sc.network.protocol)

# Organization
print(sc.organization.name)
print(sc.organization.division)
print(sc.organization.title)

## Azure
print(sc.products.azure.vm)
print(sc.products.azure.vm.details)
print(sc.products.azure.vm.metrics)
print(sc.products.azure.vm.topology)

## Elastic
print(sc.products.elastic.hits(count=1))

## QualysGuard
print(sc.products.qualysguard.scan(count=1))

## ServiceNow
print(sc.products.servicenow.search())

# User Agent
print(sc.user_agent)

# Vulnerability
print(sc.vulnerability().host)
print(sc.vulnerability().scan)
print(sc.vulnerability().data)
print(sc.vulnerability().critical)
print(sc.vulnerability().high)
print(sc.vulnerability().medium)
print(sc.vulnerability().low)
print(sc.vulnerability().informational)

# Registry
print(sc.registry.hive)
print(sc.registry.path)

# Timestamp
print(sc.timestamp.in_the_past())
print(sc.timestamp.in_the_future())
print(sc.timestamp.current)