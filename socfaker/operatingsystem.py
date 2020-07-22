from .baseclass import BaseClass


class OperatingSystem(BaseClass):

    """The OperatingSystem class contains properties commonly found within Operating Systems

    Returns:
        OperatingSystem: An object containing properties related to an operating system
    """
    _family = None
    _name = None
    _version = None

    _OS_MAP = {
        'macOS': [
            {'version': 10.0,'name': 'Cheetah'},
            {'version': 10.1,'name': 'Puma'},
            {'version': 10.2,'name': 'Jaguar'},
            {'version': 10.3,'name': 'Panther'},
            {'version': 10.4,'name': 'Tiger'},
            {'version': 10.5,'name': 'Leopard'},
            {'version': 10.6,'name': 'Snow Leopard'},
            {'version': 10.7,'name': 'Lion'},
            {'version': 10.8,'name': 'Mountain Lion'},
            {'version': 10.9,'name': 'Mavericks'},
            {'version': 10.10,'name': 'Yosemite'},
            {'version': 10.11,'name': 'El Capitan'},
            {'version': 10.12,'name': 'Sierra'},
            {'version': 10.13,'name': 'High Sierra'},
            {'version': 10.14,'name': 'Mojave'},
            {'version': 10.15,'name': 'Catalina'},
            {'version': 11.0,'name': 'Big Sur'}
        ],
        'windows':[
            {'version': '1.0', 'name': 'Windows 1'},
            {'version': '2.0', 'name': 'Windows 2'},
            {'version': '3.0', 'name': 'Windows 3'},
            {'version': '3.1x', 'name': 'Windows 3.1'},
            {'version': '3.1', 'name': 'Codename Snowball'},
            {'version': '3.11', 'name': ''},
            {'version': '95', 'name': 'Chicago'},
            {'version': '98', 'name': 'Memphis'},
            {'version': '4.9', 'name': 'Millennium Edition'},
            {'version': '3.1', 'name': 'NT'},
            {'version': '3.5', 'name': 'NT'},
            {'version': '3.51', 'name': 'NT'},
            {'version': '4.0', 'name': 'NT'},
            {'version': '2000', 'name': 'Windows NT'},
            {'version': '5.1', 'name': 'XP'},
            {'version': '5.2', 'name': 'Server 2003'},
            {'version': '6.0', 'name': 'Vista' },
            {'version': '6.0', 'name': 'Server 2008'},
            {'version': '6.1', 'name': '7'},
            {'version': '7.0', 'name': 'Phone'},
            {'version': '6.2', 'name': 'Windows 8'},
            {'version': '6.3', 'name': 'Windows 8.1'},
            {'version': '10', 'name': 'Windows 10'}
        ]
    }

    @property
    def family(self):
        """The operating system family

        Returns:
            str: Returns a random operating system family
        """
        if not self._family:
            self._family = self.random.choice([
                'macOS',
                'windows'
            ])
        return self._family

    @property
    def name(self):
        """The operating system name

        Returns:
            str: Returns a random operating system name
        """
        if not self._name:
            self._name = self.random.choice(self._OS_MAP[self.family])['name']
        return self._name

    @property
    def version(self):
        """The operating system version

        Returns:
            str: Returns a random operating system version
        """
        if not self._version:
            self._version = self.random.choice(self._OS_MAP[self.family])['version']
        return self._version

    @property
    def fullname(self):
        """The operating system full name

        Returns:
            str: Returns a random operating system full name including name, type and version
        """
        return '{family} {name} {version}'.format(
            family=self.family,
            name=self.name,
            version=self.version
        )
