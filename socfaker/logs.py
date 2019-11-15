import socket
import time
import random
import decimal
import pendulum 
from threading import Thread
from faker import Faker

from logadapter import LogAdapter

# 'a' private network class example is '10.0.0.0/8'
# 'b' private network class example is '172.16.0.0/12'
# 'c' private network class example is '192.168.0.0/16'

class Logs(Thread):

    def __init__(self, internal_ip_count=1, external_ip_count=1, private_network_class='a'):
        """Main endpoint for generating fake logs
        
        Args:
            internal_ip_count (int, optional): How many IPs in logs do you want to be internal IPs. Defaults to 1.
            external_ip_count (int, optional): How many IPs in logs do you want to be external IPs. Defaults to 1.
            private_network_class (str, optional): The private network class to use. Defaults to 'a'.

        Example: 
            logs = Logs(internal_ip_count=10, private_network_class='b')
            print(logs.generate.syslog(infected_count=2, type='ransomware'))
        """        

        super(Logs, self).__init__()
        self.fake = Faker('en_US')
        self.private_network_class = private_network_class
        self.internal_ip_list = self._internal_ips(internal_ip_count)
        self.external_ip_list = self._external_ips(external_ip_count)

        self.generate = LogAdapter(self)

    def _internal_ips(self, count=1):
        internal_ip_list = []
        for _ in range(count):
            internal_ip_list.append(self.fake.ipv4_private(address_class=self.private_network_class))
        return internal_ip_list
        
    def _external_ips(self, count=1):
        external_ip_list = []
        for _ in range(count):
            external_ip_list.append(self.fake.ipv4_public())
        return external_ip_list
