from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


class SocFaker(object):
    """The main and only entrypoint for soc-faker.

    The SocFaker class contains multiple nested properties, objects, methods, etc. to access
    and generate fake data related to security operation teams, security analysts, and any one else
    needing fake data.
    """

    @property
    def agent(self):
        """Access generated data related to an endpoint agent

        Returns:
            Agent: Returns an object with properties related to an endpoint agent
        """
        from .agent import Agent
        return Agent()

    @property
    def alert(self):
        """Alert or Detection properties

        Returns:
            Alert: Returns an object with properties about a alert or detection
        """
        from .alert import Alert
        return Alert()

    @property
    def application(self):
        """Generated data related to a application

        Returns:
            Application: Returns an object with properties about an application
        """
        from .application import Application
        return Application()

    @property
    def cloud(self):
        """Generated data related to cloud infrastructure

        Returns:
            Cloud: Returns an object with properties about cloud infrastructure
        """
        from .cloud import Cloud
        return Cloud()

    @property
    def computer(self):
        """Generated data about a computer system

        Returns:
            Computer: Returns an object with properties about a computer system
        """
        from .computer import Computer
        return Computer()

    @property
    def container(self):
        """Generated data about a container

        Returns:
            Container: Returns an object with properties about a container
        """
        from .container import Container
        return Container()

    @property
    def dns(self):
        """DNS Information

        Returns:
            DNS: Returns an object with properties about DNS request, response, etc.
        """
        from .dns import DNS
        return DNS()

    @property
    def employee(self):
        """An employee object

        Returns:
            Employee: Returns an object with properties about a fake employee
        """
        from .employee import Employee
        return Employee()

    @property
    def file(self):
        """A file object

        Returns:
            File: Returns an object with properties about a fake file object
        """
        from .file import File
        return File()

    @property
    def http(self):
        """Data related to HTTP requests and responses

        Returns:
            HTTP: Returns an object with properties about HTTP requests and responses
        """
        from .http import HTTP
        return HTTP()

    @property
    def location(self):
        """Fake location data

        Returns:
            Location: Returns an object with properties containing location information
        """
        from .location import Location
        return Location()

    @property
    def logs(self):
        """Access generated logs of different types

        Returns:
            Logs: Returns an object with properties and methods to generate fake logs
        """
        from .logs import Logs
        return Logs()

    @property
    def network(self):
        """Access common generated network information

        Returns:
            Network: Returns an object with properties containing general
            or common network information
        """
        from .network import Network
        return Network()

    @property
    def operating_system(self):
        """Fake operating system information

        Returns:
            OperatingSystem: Returns an object with properties containing
            Operating System information
        """
        from .operatingsystem import OperatingSystem
        return OperatingSystem()

    @property
    def organization(self):
        """Fake organization information

        Returns:
            Organization: Returns an object with properties containing common
            organization information
        """
        from .organization import Organization
        return Organization()

    def pcap(self, count=1):
        """Fake PCAP file is generated

        NOTE: This is still expiremental and would love any assistance
        anyone can give to make this work effectively every time

        Returns:
            PCAP: Returns generated PCAP file
        """
        from .pcap import PCAP
        return PCAP().generate(count=count)

    @property
    def process(self):
        """Fake process information

        Returns:
            Process: Returns an object with properties containing common
            process information
        """
        from .process import Process
        return Process()

    @property
    def products(self):
        """Access additional properties and methods to generate security
        related product data

        Returns:
            Products: Returns a Products object which is used to access
            product specific generated data
        """
        from .products import Products
        return Products()

    @property
    def registry(self):
        """Fake registry information

        Returns:
            Registry: Returns an object with properties containing
            common Windows registry information
        """
        from .registry import Registry
        return Registry()

    @property
    def timestamp(self):
        """Fake timestamp information

        Returns:
            Timestamp: Returns an object with methods to generate fake
            timestamps
        """
        from .timestamp import Timestamp
        return Timestamp()

    @property
    def user_agent(self):
        """Fake user agent information

        Returns:
            UserAgent: Returns an object with methods to generate fake
            user agent strings
        """
        from .useragent import UserAgent
        return UserAgent().get()

    def vulnerability(self, host_count=1, critical=1, high=1, medium=1, low=1, informational=1):
        """Generate fake vulnerability information

        Args:
            host_count (int, optional): The number of hosts to include when
                                        generating vulnerability data. Defaults to 1.
            critical (int, optional): The number of critical vulnerabilities to add. Defaults to 1.
            high (int, optional): The number of high vulnerabilities to add. Defaults to 1.
            medium (int, optional): The number of medium vulnerabilities to add. Defaults to 1.
            low (int, optional): The number of low vulnerabilities to add. Defaults to 1.
            informational (int, optional): The number of informational vulnerabilities to add.
                                           Defaults to 1.

        Returns:
            Vulnerability: Returns an object containing properties and methods to generate fake
            vulnerability related information.
        """
        from .vulnerability import Vulnerability
        return Vulnerability(
            host_count=host_count, 
            critical=critical, 
            high=high, 
            medium=medium, 
            low=low, 
            informational=informational
        )

    @property
    def words(self):
        """Used to create fake words or strings

        Returns:
            Words: Returns an object with methods to generate fake words and strings
        """
        from .words import Words
        return Words()
