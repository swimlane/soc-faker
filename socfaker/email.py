import os
from lorem_text import lorem
from .timestamp import Timestamp
from .baseclass import BaseClass
from .dns import DNS
from .network import Network
from .agent import Agent
from .employee import Employee
from .words import Words


class Email(BaseClass):

    """The Email class is designed to create random formatted eml files.

    Returns:
        Email: A Email object containing properties related to a generated eml file.
    """

    __name_list = [
        'IBM Domino Release 9.0.1FP9',
        'Postfix',
        'localhost'
    ]

    __X_HEADER_DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'email_x_headers' + '.txt'))
    __MALICIOUS_URLS = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'malicious_urls' + '.txt'))
    __MALICIOUS_DOMAINS = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'malicious_domains' + '.txt'))
    __MALICIOUS_IPS = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'malicious_ips' + '.txt'))
    __MALICIOUS_HASHES = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'malicious_hashes' + '.txt'))
    __X_HEADER_LIST = []
    __TO_ADDRESS = None
    __FROM_ADDRESS = None

    def __read_from_file(self, path):
        with open(path, 'r') as x:
            return x.readlines()

    def __get_received_from_section(self):
        esmtp = f' with ESMTP id {Agent().id}\n'
        date = Timestamp().in_the_past_pendulum_object().to_rfc2822_string()
        header = f'''Received: from {DNS().name} ([{Network().ipv4}])
            by {DNS().name} ({self.random.choice(self.__name_list)})'''
        if self.random.choice([True, False]):
            header += f"{self.random.choice([esmtp, ''])}"
        if self.random.choice([True, False]):
            header += f"\n{self.random.choice([date,''])}"
        if header.endswith('\n'):
            header += header.rstrip()
        return header

    @property
    def received_from(self):
        header_string = ''
        for i in range(self.random.randint(1,4)):
            if header_string:
                header_string += '\n'
            temp = self.__get_received_from_section()
            if self.random.choice([True, False]):
                if not self.__FROM_ADDRESS:
                    temp += f'\nfor <{Employee().email}>;'
                else:
                    temp += f'\nfor <{self.__FROM_ADDRESS}>;'
                temp += f'\n{Timestamp().in_the_past_pendulum_object().to_rfc2822_string()}'
            header_string += temp
        return header_string

    @property
    def x_headers(self):
        return_string = '\n'
        if not self.__X_HEADER_LIST:
            self.__X_HEADER_LIST = self.__read_from_file(self.__X_HEADER_DATA_PATH)
        for i in range(self.random.randint(1,5)):
            return_string += self.random.choice(self.__X_HEADER_LIST)
        return return_string.strip()

    @property
    def date(self):
        return f'Date: {Timestamp().in_the_past_pendulum_object().to_rfc2822_string()}'

    @property
    def to_address(self):
        if not self.__TO_ADDRESS:
            self.__TO_ADDRESS = Employee().email
        return self.__TO_ADDRESS

    @property
    def from_address(self):
        if not self.__FROM_ADDRESS:
            self.__FROM_ADDRESS = Employee().email
        return self.__FROM_ADDRESS

    @property
    def subject(self):
        subject_string = []
        for i in range(self.random.randint(1, 7)):
            subject_string.append(self.random.choice(Words().get()))
        return 'Subject: ' + ' '.join(subject_string).title()

    @property
    def message_id(self):
        string = ''.join([self.random.choice('0123456789ABCDEF') for x in range(32)])
        return f'Message-ID: <{string}@127.0.0.1>'

    @property
    def x_mailer(self):
        return 'X-Mailer: Outlook'

    @property
    def in_reply_to(self):
        string = ''.join([self.random.choice('0123456789ABCDEF') for x in range(32)])
        return f'In-Reply-To: <{string}@{DNS().name}>'

    @property
    def body(self):
        body_string = 'Content-Type: text/plain; charset=utf-8\n'
        body_string += 'Content-Transfer-Encoding: quoted-printable\n\n'
        for i in range(self.random.randint(1,6)):
            body_string += lorem.sentence()
        if self.random.choice([True, False]):
            body_string += f'\n\nClick Here: {self.random.choice(self.__read_from_file(self.__MALICIOUS_URLS))}'
        if self.random.choice([True, False]):
            body_string += f'\nCheck this domain out: {self.random.choice(self.__read_from_file(self.__MALICIOUS_DOMAINS))}'
        if self.random.choice([True, False]):
            body_string += f'\nMy IP address is {self.random.choice(self.__read_from_file(self.__MALICIOUS_IPS))}'
        if self.random.choice([True, False]):
            body_string += f'\n\n {self.random.choice(self.__read_from_file(self.__MALICIOUS_HASHES))}'
        return body_string

    @property
    def email(self):
        email_string = ''
        email_string += self.received_from
        email_string += f'\n{self.x_headers}'
        email_string += f'\n{self.date}'
        email_string += f'\nFrom: {self.from_address}'
        email_string += f'\nTo: {self.to_address}'
        email_string += f'\n{self.subject}'
        email_string += f'\n{self.message_id}'
        email_string += f'\n{self.x_mailer}'
        email_string += f'\n{self.in_reply_to}'
        email_string += f'\n{self.body}'
        return email_string
