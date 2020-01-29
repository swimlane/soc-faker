from .windowseventdata import WindowsEventData
from .windowseventsystem import WindowsEventSystem
from .markdowntable import MarkdownTable
from .downloadwindowseventdata import DownloadWindowsEventData
import glob, os, fnmatch
import xmltodict, random
from StringIO import StringIO
from bs4 import BeautifulSoup


class WindowsEvent(object):

    __DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'windows-event'))
    __PROVIDER_LIST = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'windows-providers' + '.txt'))

    def __init__(self, json=False):
        """Get Fake Windows Events
        
        Args:
            json (bool, optional): Converts the object to JSON from RAW XML. Defaults to False.

        Example:
            win_event = WindowsEvent(json=True)

            import json
            for item in win_event.get():
                print(json.dumps(item['Event']))
        """        
        self._get_windows_providers()

        self.file_directory = self.__check_for_event_data_cache()
        
        self.json = json


    def __check_for_event_data_cache(self):
        markdown_files = self.__check_file_directory()
        if not markdown_files:
            DownloadWindowsEventData().save()
            markdown_files = self.__check_file_directory()
        
        return markdown_files

    def __check_file_directory(self):
        matches = []
        for root, dirnames, filenames in os.walk(self.__DATA_PATH):
            for filename in fnmatch.filter(filenames, '*.md'):
                matches.append(os.path.abspath(os.path.join(root, filename)))
        return matches
    
    def _get_windows_providers(self):
        self.provider_list = []
        f = open(self.__PROVIDER_LIST, 'r')
        for x in f:
            self.provider_list.append(x.strip())

    def get(self, computer_name=None, os_type='Windows'):
        return_list = []
        for md_file in self.file_directory:
            self.soup = BeautifulSoup(features='xml')
            self.soup.append(self.soup.new_tag("Event"))
            self.markdown = MarkdownTable(md_file)
            if os_type is 'Windows':
                os_type = '1'
            else:
                os_type = '2'
            data = WindowsEventData()
            system = WindowsEventSystem(
                    random.choice(self.provider_list),
                    md_file.rsplit('/', 1)[1].split('-')[1].strip('.md'),
                    os_type,
                    computer_name
                )
            self.soup.Event.append(system.get)
            
            for rows in self.markdown.rows():
                if rows and 'Sample Value' in rows:
                    data.add(rows['Field Name'], ' ' if 'Sample Value' not in rows else rows['Sample Value'])
            
            self.soup.Event.append(data.get)
            if self.json:
                return_dict = xmltodict.parse(self.soup.prettify())
                return_list.append(return_dict)
            else:
                return_list.append(str(self.soup))
        return return_list