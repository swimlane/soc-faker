import random, requests, os, ast

from bs4 import BeautifulSoup

from .network import Network

class Alert(object):

    __DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data'))

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
        file_path = os.path.join(self.__DATA_PATH, filename)
        if not os.path.isfile(file_path):
            self.__save_location_data('https://www.symantec.com/security_response/attacksignatures/', file_path)
            return_list = self.__get_location(file_path)
        else:
            return_list = self.__get_location(file_path)
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
        file_path = os.path.join(self.__DATA_PATH, filename)
        if not os.path.isfile(file_path):
            self.__save_location_data('https://restcountries.eu/rest/v2/all', file_path)
            return_list = self.__get_location(file_path)
        else:
            return_list = self.__get_location(file_path)
        return random.choice(return_list)

    def __save_location_data(self, url, file_path):
        #print(self.__FILE_PATH)
       # print(os.listdir(os.path.join(os.path.dirname(__file__), 'data')))
        response = requests.get(url)
        if response:
            with open(file_path, 'w') as filehandle:
                if 'alert_names.txt' in file_path:
                    soup = BeautifulSoup(response.text, 'html5lib')
                    for link in soup.find_all('a'):
                        item = link.get('href')
                        if item and 'attacksignature' in item:
                            filehandle.write('{}\n'.format(link.text))
                else:
                    for item in response.json():
                        filehandle.write('{}\n'.format(item['alpha2Code']))
           
    def __get_location(self, file_path):
        return_list = []
        with open(file_path, "r") as filehandle:
            for item in filehandle.readlines():
                return_list.append(item)
        return return_list