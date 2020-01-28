# soc-faker

soc-faker is used to generate fake data for use by Security Operation Centers, Information security professionals, product teams, and many more.

## Getting Started

`soc-faker` is compatible with Python 2.x and 3.x.  You can install `soc-faker` using `pip` as well as cloning this repository directly.

At the time of writing this document, `soc-faker` has the ability to fake data for the following main categories.  You can find specific details for each category by selecting the links below:

* [Computer](faker/computer.md)
* [Application](faker/application.md)
* [Employee](faker/employee.md)
* [File](faker/file.md)
* [Logs](faker/logs.md)
* [Network](faker/network.md)
* [Organization](faker/organization.md)
* Products
    * [Azure](faker/azure.md)
    * [Elastic](faker/elastic.md)
    * [QualysGuard](faker/qualysguard.md)
    * [ServiceNow](faker/servicenow.md)
* [User Agent](faker/useragent.md)
* [Vulnerability](faker/vulnerability)
* [Alert](faker/alert.md)
* [Registry](faker/registry.md)
* [Timestamp](faker/timestamp.md)

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
   
   faker/application
   faker/azure
   faker/computer
   faker/elastic
   faker/employee
   faker/file
   faker/logs
   faker/network
   faker/organization
   faker/qualysguard
   faker/servicenow
   faker/useragent
   faker/vulnerability
```

