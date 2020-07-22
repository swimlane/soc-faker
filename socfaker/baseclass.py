import uuid, random
from faker import Faker


class BaseClass(object):

    random = random

    def __init__(self):
        #self.random = random
        self.uuid = uuid
        self._faker = Faker()

    def __str__(self):
        return_dict = {}
        for item in dir(self):
            if not item.startswith('_') and item not in self.__dict__:
                return_dict[item] = getattr(self, item)
        return str(return_dict)

    def _get_data(self, file_path):
        return_list = []
        with open(file_path, "r") as filehandle:
            for item in filehandle.readlines():
                return_list.append(item)
        return return_list