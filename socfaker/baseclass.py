import uuid, random
from faker import Faker


class BaseClass(object):

    random = random

    def __init__(self):
        self.uuid = uuid

    def __str__(self):
        return_dict = {}
        for item in dir(self):
            if not item.startswith('_') and item not in self.__dict__ and not item.startswith('random'):
                return_dict[item] = getattr(self, item)
        return str(return_dict)

    def __repr__(self):
        return_dict = {}
        for item in dir(self):
            if not item.startswith('_') and item not in self.__dict__ and not item.startswith('random'):
                return_dict[item] = getattr(self, item)
        return str(return_dict)

    def __iter__(self):
        return_dict = {}
        for item in dir(self):
            if not item.startswith('_') and item not in self.__dict__ and not item.startswith('random'):
                return_dict[item] = getattr(self, item)
        return iter(return_dict.items())

    def _get_data(self, file_path):
        return_list = []
        with open(file_path, "r") as filehandle:
            for item in filehandle.readlines():
                return_list.append(item)
        return return_list
