# soc-faker
A python package for use in generating fake data for SOC and security automation.

## Currently Implemented

* employee
* application
* organization


## TODO

### Employee

- [ ] Username (review) - add id component? 
- [x] Sex/Gender
- [ ] Employment Status?
- [x] ID
- [x] Phone Number
- [x] Email Address (based on flastname)
- [ ] Photo / RoboHash
- [x] Language
- [ ] Manager (Employee Object)
- [x] SSN
- [x] DOB

### Computer
- [ ] Operating System
- [ ] Hostname (Net)
- [ ] IP (Net)
- [ ] Disk size
- [ ] Memory 
- [ ] Networking configuration/settings
- [ ] Type (laptop, desktop, workstation, server, cloud)
- [ ] Owner
- [ ] NETBIOS



### Application
- [x] Application Status
- [x] Application Name
- [x] App Logon Timestamp

### Date
- [ ] Date Between
- [ ] Date X periods back (date after 1/1/2018)
- [ ] Date X per. Forward (date after 1/1/2018)
- [ ] Duration/Span

### Address
- [ ] Physical Address?

### Organization
- [ ] Name
- [x] Division
- [ ] Department
- [ ] Title/Job Function

### Network
- [ ] IP Address (v4/v6), private optional
- [ ] Hostname
- [ ] Physical Location
- [ ] Email Address (optional domain input)
- [ ] URL
- [ ] MAC addr

### File Info
- [ ] Filename
- [ ] File Size
- [ ] File date/timestamp
- [ ] File Hash
- [ ] Sha256
- [ ] Sha1
- [ ] Md5
- [ ] fuzzy?
- [ ] File Path
- [ ] File Reputation?
- [ ] File Extension/Type

### Logs
- [ ] Easy string format that includes objects from other classes
log.generate(**kwargs)
I.e. log.generate(date(today), workstation.name, ip.addr) -> 2019-05-13 00:00:00, KNPR-KSDFJKL, 192.1.1.1


### Vulnerability
- [ ] CVE
- [ ] Type


