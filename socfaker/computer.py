import string
from .network import Network
from .operatingsystem import OperatingSystem
from .baseclass import BaseClass


class Computer(BaseClass):

    """A computer object containing common properties about a computer

    Returns:
        Computer: An object containing common properties of a computer
    """
    _name = None
    _os = None
    __bit_shift = {
        "B": 0,
        "kb": 7,
        "KB": 10,
        "mb": 17,
        "MB": 20,
        "gb": 27,
        "GB": 30,
        "TB": 40,
    }

    @property
    def architecture(self):
        """Architecture of a computer instance

        Returns:
            str: Architecture of computer system of either x86_64 or x86
        """
        return self.random.choice([
            'x86_64', 
            'x86'
        ])

    @property
    def name(self):
        """The name of a comptuer

        Returns:
            str: A random name of a computer 
        """
        if not self._name:
            prefix = self.random.choice(['Desktop'] * 4 + ['Laptop'])
            self._name = '{}-{}'.format(prefix, ''.join(
                self.random.choice(string.ascii_uppercase + string.digits) for _ in range(7)))
        return self._name

    @property
    def disk(self):
        """The disk size of a computer instance

        Returns:
            list: Returns a list of B,KB,MB,GB, and TB size of a computers disk
        """
        return_list = []
        for item in ['B', 'KB', 'MB', 'GB', 'TB']:
            return_list.append("{:.0f}".format(self.random.randint(1, 1099511627776) / float(1 << self.__bit_shift[item])) + " " + item)
        return return_list

    @property
    def memory(self):
        """The memory size of a computer instance

        Returns:
            list: Returns a list of B,KB,MB,GB, and TB size of a computers memory size
        """
        return_list = []
        for item in ['B', 'KB', 'MB', 'GB', 'TB']:
            size = self.random.randint(1,32) * 33554432.0
            return_list.append("{:.0f}".format(size / float(1 << self.__bit_shift[item])) + " " + item)
        return return_list

    @property
    def platform(self):
        """A random name of the computers platform

        Returns:
            str: Random name of a computers platform (e.g. worksation, server, etc.)
        """
        return self.random.choice([
            'Laptop', 
            'Desktop', 
            'Workstation', 
            'Server', 
            'Virtual Machine', 
            'Container', 
            'Micro-Service', 
            'Droplet', 
            'SaaS'
        ])

    @property
    def mac_address(self):
        """A generated MAC address for a computer instance

        Returns:
            str: A random MAC Address
        """
        return_list = []
        for x in range(6):
            a = self.random.randint(0,255)
            hex = '%02x' % a
            return_list.append(hex.upper())
        return ':'.join(return_list)
        

    @property
    def os(self):
        """The operating system full name of the computer instance

        Returns:
            str: A random operating system version
        """
        if not self._os:
            self._os = OperatingSystem().fullname
        return self._os

    @property
    def ipv4(self):
        """The operating system ipv4 address

        Returns:
            str: A random operating system ipv4 address
        """
        return Network(private=True).ipv4
