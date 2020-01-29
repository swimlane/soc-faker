from lxml import etree as ET
import uuid, random, pendulum
from bs4 import BeautifulSoup

class WindowsEventSystem(object):

    '''
    Example:
        system = WindowsEventSystem('Microsoft-Windows-Security-Auditing','4688', '2', 'WIN-GG82ULGC9GO.contoso.local')

        print(str(system))
    
    Returns:
        <Event>
        <System>
            <Provider Guid="48b80978-70f3-464f-bc13-65dae959fe25" Name="Microsoft-Windows-Security-Auditing"/>
            <EventID>4688</EventID>
            <Version>2</Version>
            <Computer>WIN-GG82ULGC9GO.contoso.local</Computer>
            <Level>2</Level>
            <Task>12986</Task>
            <TimeCreated SystemTime="2016-10-29T06:33:56-05:00"/>
            <EventRecordID>2965</EventRecordID>
            <Execution ProcessID="22" ThreadID="398"/>
        </System>
        </Event>
    '''
    VERSION_MAP = {
        '0': ['Windows Server 2008', 'Windows Vista'],
        '1': ['Windows Server 2012 R2', 'Windows 8.1'],
        '2': ['Windows 10']
    }

    def __init__(self, provider, event_id, os_version, computer_name, event_level=None, task_id=None, system_time=None, event_record_id=None, process_id=None, threat_id=None):
        self.soup = BeautifulSoup(features='lxml')
        self.soup.append(self.soup.new_tag('Provider', Name=provider, Guid=str(uuid.uuid4())))

        # Setting EventId
        self._add_subelement('EventId', text=event_id)

        # Setting Version
        if os_version in self.VERSION_MAP.keys() or os_version in self.VERSION_MAP.values():
            self._add_subelement('Version', text=os_version)
        else:
            raise AssertionError('Please provide a supported OS Version: %s' % self.VERSION_MAP)

        # Setting Computer
        self._add_subelement('Computer', text=computer_name)


        if event_level:
            self._add_subelement('Level', text=event_level)
        else:
            self._add_subelement('Level', text=str(random.randint(0,4)))

        if task_id:
            self._add_subelement('Task', text=task_id)
        else:
            self._add_subelement('Task', text=str(random.randint(10000,15000)))

        if system_time:
            self._add_subelement('TimeCreated',props=('SystemTime', system_time))
        else:
            self._add_subelement('TimeCreated',props=('SystemTime', self._generate_random_timestamp()))

        if event_record_id:
            self._add_subelement('EventRecordID', text=event_record_id)
        else:
            self._add_subelement('EventRecordID', text=str(random.randint(2200,4300)))

        if process_id and threat_id:
            self._add_subelement('Execution', props=[('ProcessID', process_id),('ThreadID', threat_id)])
        else:
            self._add_subelement('Execution', props=[('ProcessID', str(random.randint(1,24))),('ThreadID', str(random.randint(200,500)))])

    def __str__(self):
        return str(self.soup)

    @property
    def get(self):
        return self.soup

    def _generate_random_timestamp(self):
        return pendulum.now().subtract(
                years=random.randint(0,3),
                months=random.randint(0,12),
                days=random.randint(1,30),
                hours=random.randint(1,23),
                minutes=random.randint(1,60),
                seconds=random.randint(1,60)
                ).to_iso8601_string()
    
    def _add_subelement(self, sub_element, text=None, props=None):
        kwargs = {}
        if props and isinstance(props,list):
            kwargs = dict(props)
            if text:
                new_tag = self.soup.new_tag(sub_element, **kwargs)
                self.soup.append(new_tag)
                new_tag.string = text
            else:
                new_tag = self.soup.new_tag(sub_element, **kwargs)
                self.soup.append(new_tag)
        elif props and isinstance(props, tuple):
            kwargs = dict([props])
            if text:
                new_tag = self.soup.new_tag(sub_element, **kwargs)
                self.soup.append(new_tag)
                new_tag.string = text
            else:
                new_tag = self.soup.new_tag(sub_element, **kwargs)
                self.soup.append(new_tag)
        elif text:
            new_tag = self.soup.new_tag(sub_element)
            self.soup.append(new_tag)
            new_tag.string = text