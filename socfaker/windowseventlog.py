from .windowseventdata import WindowsEventData
from .windowseventsystem import WindowsEventSystem
from .markdowntable import MarkdownTable
from .computer import Computer
import glob, os, fnmatch, re
import xmltodict, random
from io import StringIO
from bs4 import BeautifulSoup


class WindowsEventLog(object):

    __DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'windows-event'))
    __PROVIDER_LIST_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'windows-providers' + '.txt'))
    __file_directory = []
    __provider_list = []

    def __init__(self, json=False):
        self.json = json

    def get(self, count=1, computer_name=None, os_version='Windows'):
        return_list = []
        os_version = self.__check_os_type(os_version)
        if not computer_name:
            computer_name = Computer().name
        if not self.__file_directory:
            self.__get_file_list()
        if not self.__provider_list:
            self.__get_windows_providers()
        md_count = 0
        shuffled = random.sample(self.__file_directory, len(self.__file_directory))
        for md_file in shuffled:
            if md_count == count:
                break
            self.soup = BeautifulSoup(features='xml')
            self.soup.append(self.soup.new_tag("Event"))
            self.markdown = MarkdownTable(md_file)
            
            system = WindowsEventSystem(
                    random.choice(self.__provider_list),
                    md_file.rsplit('/', 1)[1].split('-')[1].strip('.md'),
                    os_version,
                    computer_name
                )
            self.soup.Event.append(self.soup.new_tag('System'))
            self.soup.Event.System.append(system.get)
            
            data = WindowsEventData()
            for rows in self.markdown.rows():
                if rows and 'Sample Value' in rows:
                    data.add(rows['Field Name'], ' ' if 'Sample Value' not in rows else rows['Sample Value'])

            self.soup.Event.append(self.soup.new_tag('EventData'))
            self.soup.Event.EventData.append(data.get)
            
            if self.json:
                soup_string = self.soup.prettify()
                return_dict = xmltodict.parse(soup_string.strip())
                return_list.append(return_dict)
            else:
                return_list.append(self.soup.prettify())
            md_count += 1
        return return_list

    def __get_windows_providers(self):
        self.__provider_list = []
        f = open(self.__PROVIDER_LIST_PATH, 'r')
        for x in f:
            self.__provider_list.append(x.strip())

    def __check_os_type(self, os_version):
        if os_version in ['Windows Server 2008', 'Windows Vista']:
            return '0'
        elif os_version in ['Windows Server 2012 R2', 'Windows 8.1']:
            return '1'
        elif os_version in ['Windows 10']:
            return '2'
        else:
            return str(random.randint(0,2))

    def __get_file_list(self):
        for root, dirnames, filenames in os.walk(self.__DATA_PATH):
            for filename in fnmatch.filter(filenames, '*.md'):
                self.__file_directory.append(os.path.abspath(os.path.join(root, filename)))
