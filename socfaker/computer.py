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
        disk_size_list = []
        precision = 2
        size = self.random.randint(1, 1099511627776)
        suffixes=['B','KB','MB','GB','TB']
        suffixIndex = 0
        while size > 1024 and suffixIndex < 4:
            suffixIndex += 1 #increment the index of the suffix
            size = size/1024.0 #apply the division
            disk_size_list.append("%.*f{}".format((precision,size,suffixes[suffixIndex])))
        return disk_size_list

    @property
    def memory(self):
        """The memory size of a computer instance

        Returns:
            list: Returns a list of B,KB,MB,GB, and TB size of a computers memory size
        """
        mem_size_list = []
        precision = 2
        gig_size = self.random.randint(1,32)
        size = gig_size * 1073741824
        suffixes=['B','KB','MB','GB','TB']
        suffixIndex = 0
        while size > 1024 and suffixIndex < 4:
            suffixIndex += 1 #increment the index of the suffix
            size = size/1024.0 #apply the division
            mem_size_list.append("%.*f{}".format((precision,size,suffixes[suffixIndex])))
        return mem_size_list

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
        return ':'.join("{}02x".format(self.random.randint(0, 255) for _ in range(5)))

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
