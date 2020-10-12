# soc-faker

soc-faker is used to generate fake data for use by Security Operation Centers, Information security professionals, product teams, and many more.

## Getting Started

`soc-faker` is compatible with Python 2.x and 3.x.  You can install `soc-faker` using `pip` as well as cloning this repository directly.

At the time of writing this document, `soc-faker` has the ability to fake data for the following main categories.  You can find specific details for each category by selecting the links below:

* [Agent](faker/agent.md)
* [Alert](faker/alert.md)
* [Application](faker/application.md)
* [Cloud](faker/cloud.md)
* [Computer](faker/computer.md)
* [Container](faker/container.md)
* [DNS](faker/dns.md)
* [Employee](faker/employee.md)
* [File](faker/file.md)
* [HTTP](faker/http.md)
* [Location](faker/location.md)
* [Logs](faker/logs.md)
    * [SysMon](faker/sysmon.md)
    * [Windows Event Logs](faker/eventlog.md)
* [Network](faker/network.md)
* [Operating System](faker/operating_system.md)
* [Organization](faker/organization.md)
* [PCAP](faker/pcap.md)
* [Process](faker/process.md)
* Products
    * [AlienVault USM](faker/alienvaultusm.md)
    * [Azure](faker/azure.md)
    * [Elastic](faker/elastic.md)
    * [QualysGuard](faker/qualysguard.md)
    * [ServiceNow](faker/servicenow.md)
* [Registry](faker/registry.md)
* [Timestamp](faker/timestamp.md)
* [TLS](faker/tls.md)
* [Url](faker/url.md)
* [User Agent](faker/useragent.md)
* [Vulnerability](faker/vulnerability)
* [Words](faker/words.md)

### Installing soc-faker

```bash
pip install soc-faker --user
```

### Installing from source

```bash
git clone https://github.com/swimlane/soc-faker.git
cd soc-faker
python setup.py install
```

### Prerequisites

The following libraries are required and installed by soc-faker

```
requests==2.23.0
pendulum==1.2.5
ipaddress==1.0.23
networkx==2.4
matplotlib==3.3.0rc1
bs4==0.0.1
lxml==4.5.1
xmltodict==0.12.0
netaddr==0.7.20
fire==0.3.1
```

## Using soc-faker

`soc-faker` is a Python package that can be imported or be used via the command line utility to generate fake data related to security tools, products, and general data related to security.

After you have installe `soc-faker` you can import and instantiate it by doing the following:

```python
from socfaker import SocFaker

sc = SocFaker()
```

Once you have instantiated an instance of `soc-faker` you can then access any of the different properties and methods avaialble based on your needs. If you would like to see soc-faker in action, then please see the script in the repository under the `bin` folder for an example of all avaialble properties and methods.

Additionally, please read the documentation for more details about each avaialble property and method.

### Development

You can use the provided [Dockerfile](Dockerfile) to get a development and testing environment up and running for `soc-faker`.

To use the `Dockerfile` run, cd to this repositories directory and run:

```
docker build --force-rm -t socfaker .
```

Once it is built, then run the docker container:

```
docker run socfaker
```

Running this will call the test python file in [bin\test.py](bin\test.py).  Modify this file for additional testing and development.


## Running the tests

Tests within this project should cover all available properties and methods.  As this project grows the tests will become more robust but for now we are testing that they exist and return outputs.

## Built With

* [carcass](https://github.com/MSAdministrator/carcass) - Python packaging template

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. 

## Change Log

Please read [CHANGELOG.md](CHANGELOG.md) for details on features for a specific version of `soc-faker`

## Authors

* Josh Rickard - *Initial work* - [MSAdministrator](https://github.com/msadministrator)
* Nick Tausek

See also the list of [contributors](https://github.com/{github_username}/{package_name}/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details

## Credits

`soc-faker` is a [Swimlane](https://swimlane.com) open-source project; we believe in giving back to the open-source community by sharing some of the projects we build for our application. Swimlane is an automated cyber security operations and incident response platform that enables cyber security teams to leverage threat intelligence, speed up incident response and automate security operations.

[SecOps Hub](https://secopshub.com) is an open, product-agnostic, online community for security professionals to share ideas, use cases, best practices, and incident response strategies.

## Acknowledgments

* This project utilizes data from the OSSEM project by [hunters-forge](https://github.com/hunters-forge/OSSEM)

```eval_rst
.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   faker/agent
   faker/alert
   faker/application
   faker/azure
   faker/cloud
   faker/computer
   faker/container
   faker/dns
   faker/elastic
   faker/employee
   faker/file
   faker/http
   faker/location
   faker/logs
   faker/network
   faker/organization
   faker/operating_system
   faker/qualysguard
   faker/registry
   faker/servicenow
   faker/sysmon
   faker/timestamp
   faker/useragent
   faker/vulnerability
   faker/words
```

