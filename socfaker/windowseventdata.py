from bs4 import BeautifulSoup
import uuid, random, pendulum


class WindowsEventData(object):
    '''
    Example: 
        evt_data = WindowsEventData()
        evt_data.add('SubjectUserName', 'WIN-GG82ULGC9GO$')
        evt_data.add('NewProcessName', 'C:\Windows\System32rundll32.exe')
        print(ET.dump(evt_data.data))

    Returns:
        <EventData>
            <Data Name="SubjectUserName">WIN-GG82ULGC9GO$</Data>
            <Data Name="NewProcessName">C:\Windows\System32rundll32.exe</Data>
        </EventData>
    '''
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