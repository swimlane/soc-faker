import random, requests, os, ast

from bs4 import BeautifulSoup

from .network import Network

class Alert(object):

    @property
    def summary(self):
        return '{status} {action} {type} {direction} {location}'.format(
            status=self.status,
            action=self.action,
            type=self.type,
            direction=self.direction,
            location=self.location
        )
        
    @property
    def signature_name(self):
        return_list = []
        filename = 'alert_names.txt'
        if not os.path.isfile('./data/{}'.format(filename)):
            self.__save_location_data('https://www.symantec.com/security_response/attacksignatures/', filename)
            return_list = self.__get_location(filename)
        else:
            return_list = self.__get_location(filename)
        return random.choice(return_list)

    @property
    def type(self):
        return random.choice(['network', 'host', 'correlation', 'security endpoint'])

    @property
    def status(self):
        return random.choice(['successful', 'unsuccessful'])

    @property
    def action(self):
        return random.choice(['connection', 'dropped connection', 'initiated'])

    @property
    def direction(self):
        return random.choice(['from', 'to'])

    @property
    def location(self):
        return_list = []
        filename = 'country.txt'
        if not os.path.isfile('./data/{}'.format(filename)):
            self.__save_location_data('https://restcountries.eu/rest/v2/all', filename)
            return_list = self.__get_location(filename)
        else:
            return_list = self.__get_location(filename)
        return random.choice(return_list)

    def __save_location_data(self, url, filename):
        response = requests.get(url)
        if response:
            with open('./data/{}'.format(filename), 'w') as filehandle:
                if filename == 'alert_names.txt':
                    soup = BeautifulSoup(response.text, 'html5lib')
                    for link in soup.find_all('a'):
                        item = link.get('href')
                        if item and 'attacksignature' in item:
                            filehandle.write('{}\n'.format(link.text))
                else:
                    for item in response.json():
                        filehandle.write('{}\n'.format(item['alpha2Code']))
           
    def __get_location(self, filename):
        return_list = []
        with open("./data/{}".format(filename), "r") as filehandle:
            for item in filehandle.readlines():
                return_list.append(item)
        return return_list