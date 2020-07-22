import os, csv
from .baseclass import BaseClass


class Location(BaseClass):

    """The Location object contains information about location information

    Returns:
        Location: Returns a Location object contain properties about location information
    """
    __location_list = []
    __DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'locations.csv'))

    def __init__(self):
        super(Location, self).__init__()
        if not self.__location_list:
            self.__get_locations()
        self.__location = self.random.choice(self.__location_list)
        
    def __get_locations(self):
        if not self.__location_list:
            try:
                reader = csv.DictReader(open(self.__DATA_PATH, 'r', encoding='utf-8-sig'))
            except:
                reader = csv.DictReader(open(self.__DATA_PATH, 'r'))
            for line in reader:
                temp_dict = {}
                for key in line.keys():
                    temp_dict[key.strip()] = line[key]
                self.__location_list.append(dict(temp_dict))

    @property
    def latitude(self):
        """Random Latitude coordinates

        Returns:
            str: Returns a random latitude coordinates
        """
        return self.__location.get('latitude')

    @property
    def longitude(self):
        """Random Longitude coordinates

        Returns:
            str: Returns a random longitude coordinates
        """
        return self.__location.get('longitude')

    @property
    def city(self):
        """A random city

        Returns:
            str: Returns a random city name
        """
        return self._faker.city()
    
    @property
    def continent(self):
        """A random continent

        Returns:
            str: Returns a random continent
        """
        return self.random.choice(['Asia', 'Africa', 'North America', 'South America', 'Antarctica', 'Europe', 'Australia'])

    @property
    def country_code(self):
        """A random country code

        Returns:
            str: Returns a random country code
        """
        return self.__location.get('country')
    
    @property
    def country(self):
        """A random country

        Returns:
            str: Returns a random country
        """
        return self.__location.get('name')
