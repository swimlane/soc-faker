import os, json
from .baseclass import BaseClass


class Location(BaseClass):

    """The Location object contains information about location information

    Returns:
        Location: Returns a Location object contain properties about location information
    """
    __location_list = []
    __DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'locations.json'))

    def __init__(self):
        super(Location, self).__init__()
        if not self.__location_list:
            self.__get_locations()
        self.__location = self.random.choice(self.__location_list)
        
    def __get_locations(self):
        if not self.__location_list:
            with open(self.__DATA_PATH, 'r') as file:
                for item in json.load(file):
                    self.__location_list.append(item)

    @property
    def latitude(self):
        """Random Latitude coordinates

        Returns:
            str: Returns a random latitude coordinates
        """
        return float(self.__location.get('latlng')[0])

    @property
    def longitude(self):
        """Random Longitude coordinates

        Returns:
            str: Returns a random longitude coordinates
        """
        return float(self.__location.get('latlng')[1])

    @property
    def city(self):
        """A random city

        Returns:
            str: Returns a random city name
        """
        return self.__location.get('capital')
    
    @property
    def continent(self):
        """A random continent

        Returns:
            str: Returns a random continent
        """
        return self.__location.get('region')

    @property
    def country_code(self):
        """A random country code

        Returns:
            str: Returns a random country code
        """
        return self.__location.get('alpha2Code')
    
    @property
    def country(self):
        """A random country

        Returns:
            str: Returns a random country
        """
        return self.__location.get('name')
