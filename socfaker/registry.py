from .baseclass import BaseClass


class Registry(BaseClass):

    __hives = [
        'HKEY_CURRENT_USER',
        'HKEY_LOCAL_MACHINE',
        'HKEY_USERS'
    ]
    __root = None
    __hive = None
    __key = None

    @property
    def hive(self):
        """A random registry hive

        Returns:
            str: Returns a random registry hive
        """
        if not self.__hive:
            self.__hive = self.random.choice(self.__hives)
        return self.__hive

    @property
    def root(self):
        """A random registry root path string

        Returns:
            str: Returns a random registry root path string
        """
        if not self.__root:
            self.__root = self.random.choice([
                'SOFTWARE',
                'SECURITY',
                'SYSTEM'
            ])
        return self.__root

    @property
    def key(self):
        """A random registry key

        Returns:
            str: Returns a random registry key
        """
        if not self.__key:
            NEXT_LEVEL = [
                'POLICIES',
                'CLASSES',
                'SETUP',
                'SOFTWARE'
            ]
            PRODUCT = [
                'MICROSOFT\\Windows\\CurrentVersion\\RunOnce\\',
                'ADOBE',
                'GOOGLE',
                'ORACLE'
            ]
            KEYS = [
                'RUN',
                'OPEN',
                'SET'
            ]
            self.__key = '{}\\{}\\{}\\{}'.format(self.random.choice(self.root), self.random.choice(NEXT_LEVEL), self.random.choice(PRODUCT), self.random.choice(KEYS))
        return self.__key

    @property
    def path(self):
        """A full registry path
        
        Returns:
            str: Returns a random full registry path
        """
        return '{}\\{}'.format(self.hive, self.key)

    @property
    def type(self):
        """A random registry key type

        Returns:
            str: A random registry key type
        """
        return self.random.choice([
            'REG_SZ',
            'REG_DWORD',
            'REG_EXPAND_SZ',
            'REG_MULTI_SZ',
            'REG_BINARY'
        ])

    @property
    def value(self):
        """A random registry key value

        Returns:
            str: A random registry key value
        """
        return self.random.choice([
            'Debugger',
            'Enabled',
            'Disabled',
            'Unknown',
            1,
            0
        ])
