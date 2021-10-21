from bs4 import BeautifulSoup


class WindowsEventData(object):

    def __init__(self):
        self.data_list = []
        self.soup = BeautifulSoup(features='lxml')

    @property
    def get(self):
        return self.soup

    def add(self, name, text):
        new_tag = self.soup.new_tag(name)
        self.soup.append(new_tag)
        new_tag.string = text
