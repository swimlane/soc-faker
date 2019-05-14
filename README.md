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
- [x] Employment Status?
- [x] ID
- [x] Phone Number
- [x] Email Address (based on flastname)
- [ ] Photo / RoboHash
- [x] Language
- [ ] Manager (Employee Object)
- [x] SSN
- [x] DOB

### Computer
- [x] Operating System
- [x] Hostname (Net)
- [ ] IP (Net)
- [x] Disk size
- [x] Memory 
- [ ] Networking configuration/settings
- [x] Type (laptop, desktop, workstation, server, cloud)
- [ ] Owner
- [x] NETBIOS



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
- [x] Name
- [x] Division
- [ ] Department
- [x] Title/Job Function

### Network
- [x] IP Address (v4/v6), private optional
- [x] Hostname
- [ ] Physical Location
- [ ] Email Address (optional domain input)
- [ ] URL
- [x] MAC addr

### File Info
- [x] Filename
- [x] File Size
- [x] File date/timestamp
- [x] Sha256
- [x] Sha1
- [x] Md5
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


