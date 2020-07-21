from socfaker import SocFaker

sc = SocFaker()

# Agent
print(sc.agent.ephermeral_id)
print(sc.agent.id)
print(sc.agent.type)
print(sc.agent.name)
print(sc.agent.version)
print(sc.agent)

# Alert
print(sc.alert.summary)
print(sc.alert.signature_name)
print(sc.alert.type)
print(sc.alert.status)
print(sc.alert.action)
print(sc.alert.direction)
print(sc.alert.location)

# Application
print(sc.application.status)
print(sc.application.account_status)
print(sc.application.name)
print(sc.application.logon_timestamp)

# Cloud 
print(sc.cloud.id)
print(sc.cloud.zone)
print(sc.cloud.instance_id)
print(sc.cloud.name)
print(sc.cloud.size)
print(sc.cloud.provider)
print(sc.cloud.region)

# Computer
print(sc.computer.architecture)
print(sc.computer.name)
print(sc.computer.disk)
print(sc.computer.memory)
print(sc.computer.platform)
print(sc.computer.mac_address)
print(sc.computer.os)

# Container
print(sc.container.id)
print(sc.container.name)
print(sc.container.tags)
print(sc.container.runtime)

# DNS
print(sc.dns.record)
print(sc.dns.header_flags)
print(sc.dns.id)
print(sc.dns.response_code)
print(sc.dns.op_code)
print(sc.dns.answers)
print(sc.dns.question)
print(sc.dns.direction)
print(sc.dns.name)

# Employee
print(sc.employee.name)
print(sc.employee.first_name)
print(sc.employee.last_name)
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

# HTTP
print(sc.http.request)
print(sc.http.response)
print(sc.http.status_code)
print(sc.http.method)
print(sc.http.bytes)

# Location
print(sc.location.latitude)
print(sc.location.longitude)
print(sc.location.city)
print(sc.location.continent)
print(sc.location.country_code)
print(sc.location.country)

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
print(sc.network.port)
print(sc.network.protocol)

# Operating System
print(sc.operating_system.family)
print(sc.operating_system.name)
print(sc.operating_system.version)
print(sc.operating_system.fullname)

# Organization
print(sc.organization.name)
print(sc.organization.domain)
print(sc.organization.division)
print(sc.organization.title)

# PCAP
print(sc.pcap())

# Process 
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

# Registry
print(sc.registry.hive)
print(sc.registry.root)
print(sc.registry.key)
print(sc.registry.path)
print(sc.registry.type)
print(sc.registry.value)

# Timestamp
print(sc.timestamp.in_the_past())
print(sc.timestamp.in_the_future())
print(sc.timestamp.current)
print(sc.timestamp.date_string())

# Products

## Azure
print(sc.products.azure.vm)
print(sc.products.azure.vm.details)
print(sc.products.azure.vm.metrics)
print(sc.products.azure.vm.metrics.average)
print(sc.products.azure.vm.metrics.graphs)
print(sc.products.azure.vm.topology)

## Elastic
print(sc.products.elastic.hits(count=1))
print(sc.products.elastic.document(count=1))



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

# Words
print(sc.words.get())
