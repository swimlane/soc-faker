import json, os
from .network import Network
from .words import Words
from .baseclass import BaseClass


class DNS(BaseClass):

    """The DNS class contains common information related to DNS data

    Returns:
        DNS: An object containing information related to DNS
    """
    __TLD_DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'tld' + '.json'))
    __WORDS_DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'words' + '.txt'))
    __WORD_LIST = Words().get()
    __TLD_LIST = []
    _network = Network()
     
    @property
    def record(self):
        """A randomly selected record type

        Returns:
            str: A random DNS record (e.g. A, CNAME, PTR, etc.)
        """
        return self.random.choice([
            'A',
            'AAAA',
            'ALIAS',
            'CNAME',
            'MX',
            'NS',
            'PTR',
            'SOA',
            'SRV',
            'TXT'
        ])

    @property
    def header_flags(self):
        """DNS Header flags

        Returns:
            str: A randomly selected DNS Header Flag
        """
        return self.random.choice([
            'AA',
            'TC',
            'RD',
            'RA',
            'AD',
            'CD',
            'DO'
        ])

    @property
    def id(self):
        """A random DNS ID value from 10000,100000

        Returns:
            int: A random DNS ID value
        """
        return self.random.randint(10000,100000)

    @property
    def response_code(self):
        """A DNS Response Code

        Returns:
            str: A DNS response code as part of a response made during a DNS request
        """
        return self.random.choice([
            'NOERROR',
            'NXDOMAIN',
            'SERVFAIL',
            'REFUSED'
        ])
    
    @property
    def op_code(self):
        """A DNS OP COde

        Returns:
            str: A random DNS OP Code for a DNS request
        """
        return self.random.choice([
            'QUERY',
            'IQUERY',
            'STATUS',
            'NOTIFY',
            'UPDATE',
            'DSO'
        ])

    def __get_dns_answer(self):
        return {
            'class': 'IN',
            'data': self._network.ipv4,
            'name': self._network.hostname,
            'ttl': self.random.randint(10,400),
            'type': self.record
        }

    @property
    def answers(self):
        """A list of DNS answers during a DNS request

        Returns:
            list: A random list (count) of random DNS answers during a DNS request
        """
        return_list = []
        for i in range(self.random.randint(1,8)):
            return_list.append(self.__get_dns_answer())
        return return_list

    @property
    def question(self):
        """A DNS question during a DNS request

        Returns:
            dict: A random DNS question during a DNS request
        """
        return self.__get_dns_answer()

    @property
    def direction(self):
        """The direction of a DNS request

        Returns:
            str: Returns a direction for a DNS request or response
        """
        return self.random.choice([
            'inbound',
            'outbound',
            'internal',
            'external',
            'unknown'
        ])

    @property
    def name(self):
        """Returns a randomly generated DNS name

        Returns:
            str: A random DNS Name
        """
        if not self.__TLD_LIST:
            with open(self.__TLD_DATA_PATH, 'r') as tlds:
                data = json.load(tlds)
                for key,val in data.items():
                    self.__TLD_LIST.append(val)
        try:
            tld = self.random.choice(self.__TLD_LIST)
        except:
            tld = self.random.choice(self.__TLD_LIST).encode('utf-8')
        return "{}.{}.{}".format(
            self.random.choice(self.__WORD_LIST),
            self.random.choice(self.__WORD_LIST),
            tld
            )
