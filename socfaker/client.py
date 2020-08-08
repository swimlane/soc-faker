from .useragent import UserAgent
from .network import Network

class Client(object):

    def get(self, number):
        ip_list=[]
        ua_list=[]
        i=0
        while i < number:
            ip_list.append(Network().ipv4)
            ua_list.append(UserAgent().get())
            i += 1
        client_list = dict( zip(ip_list,ua_list ))
        return client_list
