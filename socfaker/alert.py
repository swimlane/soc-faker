import requests, os, ast
from bs4 import BeautifulSoup
from .network import Network
from .location import Location
from .baseclass import BaseClass


class Alert(BaseClass):

    """The Alert class is designed to mimc common information contained
       within a detection or alert.

    Returns:
        Alert: A Alert object containing property related to a 
               detection or alert
    """

    __DATA_PATH = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), 'data', 'alert_names' + '.txt'
        )
    )
    _url = 'https://www.symantec.com/security_response/attacksignatures/'
    __signature_name_list = []
    _location = Location()

    @property
    def summary(self):
        """Returns the summary of an alert

        Returns:
            str: Returns a string of this instance of an alert.  
                 Contains a status, action, type, direction, and location.
        """
        return '{status} {action} {type} {direction} {location}'.format(
            status=self.status,
            action=self.action,
            type=self.type,
            direction=self.direction,
            location=self.location
        )

    @property
    def signature_name(self):
        """Returns the name of a signature that the Alert triggered upon

        Returns:
            Str: returns a random alert signature name
        """
        if not self.__signature_name_list:
            if not os.path.isfile(self.__DATA_PATH):
                self.__save_location_data(self._url, self.__DATA_PATH)
                self.__signature_name_list = self._get_data(self.__DATA_PATH)
            else:
                self.__signature_name_list = self._get_data(self.__DATA_PATH)
        return self.random.choice(self.__signature_name_list)

    @property
    def type(self):
        """Returns an alert type

        Returns:
            str: Returns a random alert type
        """
        return self.random.choice([
            'network', 
            'host', 
            'correlation', 
            'security endpoint'
        ])

    @property
    def status(self):
        """The current alert status

        Returns:
            str: Returns whether the alert was successful 
                 or unsuccessful
        """
        return self.random.choice(['successful', 'unsuccessful'])

    @property
    def action(self):
        """An action taken based on the alert

        Returns:
            str: Returns a random action based on the alert
        """
        return self.random.choice([
            'connection', 
            'dropped connection', 
            'initiated'
        ])

    @property
    def direction(self):
        """The direction of the alert (network based)

        Returns:
            str: Random direction of from or to
        """
        return self.random.choice(['from', 'to'])

    @property
    def location(self):
        """The country the alert originated from

        Returns:
            str: A random country an alert was generated from
        """
        return self._location.country

    def __save_location_data(self, url, file_path):
        response = requests.get(url)
        if response:
            with open(file_path, 'w') as filehandle:
                if 'alert_names.txt' in file_path:
                    soup = BeautifulSoup(response.text, 'html5lib')
                    for link in soup.find_all('a'):
                        item = link.get('href')
                        if item and 'attacksignature' in item:
                            filehandle.write('{}\n'.format(link.text))
