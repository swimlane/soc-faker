import random

__HIVES__ = [
    'HKEY_CURRENT_USER',
    'HKEY_LOCAL_MACHINE',
    'HKEY_USERS'
]

class Registry(object):

    def __init__(self):
        self.hive = ''
  

    @property
    def hive(self):
        return self.__hive

    @hive.setter
    def hive(self, value):
        self.__hive = random.choice(__HIVES__)

    @property
    def path(self):
        ROOT = [
            'SOFTWARE',
            'SECURITY',
            'SYSTEM'
        ]
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
        return '{}\\{}\\{}\\{}\\{}'.format(self.hive, random.choice(ROOT), random.choice(NEXT_LEVEL), random.choice(PRODUCT), random.choice(KEYS))

