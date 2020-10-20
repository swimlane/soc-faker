# soc-faker

soc-faker is used to generate fake data for use by Security Operation Centers, Information security professionals, product teams, and many more.

## Getting Started

`soc-faker` is compatible with Python 2.x and 3.x.  You can install `soc-faker` using `pip` as well as cloning this repository directly.

At the time of writing this document, `soc-faker` has the ability to fake data for the following main categories.  You can find specific details for each category by selecting the links below:

* [Agent](docs/source/faker/agent.md)
* [Alert](docs/source/faker/alert.md)
* [Application](docs/source/faker/application.md)
* [Cloud](docs/source/faker/cloud.md)
* [Computer](docs/source/faker/computer.md)
* [Container](docs/source/faker/container.md)
* [DNS](docs/source/faker/dns.md)
* [Employee](docs/source/faker/employee.md)
* [File](docs/source/faker/file.md)
* [HTTP](docs/source/faker/http.md)
* [Location](docs/source/faker/location.md)
* [Logs](docs/source/faker/logs.md)
    * [SysMon](docs/source/faker/sysmon.md)
    * [Windows Event Logs](docs/source/faker/eventlog.md)
* [Network](docs/source/faker/network.md)
* [Operating System](docs/source/faker/operating_system.md)
* [Organization](docs/source/faker/organization.md)
* [PCAP](docs/source/faker/pcap.md)
* [Process](docs/source/faker/process.md)
* Products
    * [AlienVault USM](docs/source/faker/alienvaultusm.md)
    * [Azure](docs/source/faker/azure.md)
    * [Elastic](docs/source/faker/elastic.md)
    * [QualysGuard](docs/source/faker/qualysguard.md)
    * [ServiceNow](docs/source/faker/servicenow.md)
* [Registry](docs/source/faker/registry.md)
* [Timestamp](docs/source/faker/timestamp.md)
* [TLS](docs/source/faker/tls.md)
* [Url](docs/source/faker/url.md)
* [User Agent](docs/source/faker/useragent.md)
* [Vulnerability](docs/source/faker/vulnerability)
* [Words](docs/source/faker/words.md)


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
pendulum==2.1.2
ipaddress==1.0.23
bs4==0.0.1
lxml==4.5.1
xmltodict==0.12.0
netaddr==0.7.20
fire==0.3.1
```

## Usage

`soc-faker` is a Python package that can be imported or be used via the command line utility to generate fake data related to security tools, products, and general data related to security.

### Importing soc-faker

After you have installed `soc-faker` from source or using `pip` you can import and instantiate it by doing the following:

```python
from socfaker import SocFaker

sc = SocFaker()
```

Once you have instantiated an instance of `soc-faker` you can then access any of the [different properties and methods](docs/source/index.md) avaialble based on your needs. If you would like to see soc-faker in action, then please see the [bin/test.py](bin/test.py) script in the repository under the `bin` folder for an example of all avaialble properties and methods.

Additionally, please read the [documentation](docs/source/index.md) for more details about each avaialble property and method.

### Command-Line Usage

When `soc-faker` is installed, it automatically creates a command-line utility for your use.  This utility can be accessed by simply typing `soc-faker` in your shell of choice.  

To see `soc-faker` help type:

```bash
soc-faker
# or
soc-faker --help
```

You can access each property just like you can from the library, the only difference is you replace a `.` between properties with a space.  For example, if you wanted to get some randomly generated `hashes` quickly you can run:

```bash
soc-faker file hashes
```

This will return the following to your shell:


```output
md5:    aa3150ac34ee6a5911e61ab6a5052a6d
sha1:   de5c15f64d979ed84bac340c334a63d94401059d
sha256: 118a9f9de8f3dd6471ef113959485ecbaf66368dea16758eab4e22da182d0e9f
```

If you run into any issues, just type what you think is correct and the built-in help will guide you through all available groups, commands, etc. for each data point within `soc-faker`.

### Development

You can use the provided [Dockerfile](Dockerfile) to get a development and testing environment up and running for `soc-faker`.

To use the `Dockerfile` run, cd to this repositories directory and run:

```
docker build --force-rm -t socfaker .
```

Once it is built, then run the docker container:

```
docker run -p 7001:7001 -ti socfaker
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
