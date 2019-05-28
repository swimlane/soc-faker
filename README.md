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

- [x] Critical Vulns
- [x] High Vulns
- [x] Medium Vulns
- [x] Low Vulns
- [x] Informational Vulns

### Vulnerability Host

- [x] Host ID
- [x] Name
- [x] Checks Considered
- [x] Percentage of vulns vs checks considered
- [x] Total Vuln Score for this host

### Vulnerability Scan

- [x] Scan Name
- [x] Scanner Name
- [x] Scan Type
- [x] Scan Status
- [x] Scan ID
- [x] Scan UUID
- [x] Scan Start Time 
- [x] Scan End Time 
- [x] Host Count
- [x] IP List for Scan
