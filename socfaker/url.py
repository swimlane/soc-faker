import os
from .baseclass import BaseClass
from .dns import DNS
from .employee import Employee
from .computer import Computer


class Url(BaseClass):

    # Formats were borrowed from Faker python package
    # https://github.com/joke2k/faker/blob/ced876f8dfd951c4e6fdbc7188f222bac1b235b2/faker/providers/internet/__init__.py
    
    __DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'uri' + '.txt'))
    __uri_data = []
    __netloc = None

    def __init__(self):
        super(Url, self).__init__()
        self.__get_data()

    def __get_data(self):
        if not self.__uri_data:
            with open(self.__DATA_PATH, 'r') as file:
                for item in file.readlines():
                    self.__uri_data.append(item.strip())

    @property
    def scheme(self):
        return self.random.choice([
            'http',
            'https',
            'ftp',
            'sftp'
        ])

    @property
    def netloc(self):
        if not self.__netloc:
            self.__netloc = "{www}{domain}:{port}/{path}{params}/{query}".format(
                www=self.random.choice(['www','']),
                domain=DNS().name,
                path=self.path,
                params=self.params,
                query=self.query,
                port=self.port
            )
        return self.__netloc

    @property
    def path(self):
        return self.random.choice(self.__uri_data)
    
    @property
    def params(self):
        return ';' + self.random.choice([
            'id',
            'name',
            'ids',
            'type'
        ])

    @property
    def query(self):
        query_list = []
        for i in range(self.random.randint(1,3)):
            if i == 1:
                query_list.append('id={}'.format(str(self.uuid.uuid4())))
            if i == 2:
                query_list.append('name={}'.format(Employee().name))
            if i == 3:
                query_list.append('os={}'.format(Computer().os))
        return '?' + '&'.join([x for x in query_list])

    @property
    def port(self):
        return self.random.choice(['80', '443'])

    @property
    def url(self):
        return self.scheme + '://' + self.netloc
