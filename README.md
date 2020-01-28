# soc-faker

soc-faker is used to generate fake data for use by Security Operation Centers, Information security professionals, product teams, and many more.

## Getting Started

`soc-faker` is compatible with Python 2.x and 3.x.  You can install `soc-faker` using `pip` as well as cloning this repository directly.

At the time of writing this document, `soc-faker` has the ability to fake data for the following main categories.  You can find specific details for each category by selecting the links below:

* [Alert](docs/source/faker/alert.md)
* [Computer](docs/source/faker/computer.md)
* [Application](docs/source/faker/application.md)
* [Employee](docs/source/faker/employee.md)
* [File](docs/source/faker/file.md)
* [Logs](docs/source/faker/logs.md)
* [Network](docs/source/faker/network.md)
* [Organization](docs/source/faker/organization.md)
* Products
    * [Azure](docs/source/faker/azure.md)
    * [Elastic](docs/source/faker/elastic.md)
    * [QualysGuard](docs/source/faker/qualysguard.md)
    * [ServiceNow](docs/source/faker/servicenow.md)
* [User Agent](docs/source/faker/useragent.md)
* [Vulnerability](docs/source/faker/vulnerability)
* [Registry](docs/source/faker/registry.md)
* [Timestamp](docs/source/faker/timestamp.md)

### Installing soc-faker

```bash
pip install soc-faker --user
```

### Installing from source

```bash
git clone git@github.com:swimlane/soc-faker.git
cd soc-faker
python setup.py install
```

### Prerequisites

The following libraries are required and installed by soc-faker

```
requests
pendulum
ipaddress
Pillow
networkx
matplotlib
PyGithub
PyYAML
Faker
```

### GitHub PAT

In addition, you must provide a GitHub Personal Access Token to utilize specific features that rely on data from public github repositories.

Please follow this guide to get a personal access token [https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line)

Once you have a PAT you can provide this token during initialization of the the `SocFaker` object:

```
from socfaker import SocFaker

sf = SocFaker(github_token='YOUR PERSONAL ACCESS TOKEN')
```

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
   
   docs/source/faker/application
   docs/source/faker/azure
   docs/source/faker/computer
   docs/source/faker/elastic
   docs/source/faker/employee
   docs/source/faker/file
   docs/source/faker/logs
   docs/source/faker/network
   docs/source/faker/organization
   docs/source/faker/qualysguard
   docs/source/faker/servicenow
   docs/source/faker/useragent
   docs/source/faker/vulnerability
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