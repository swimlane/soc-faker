from .baseclass import BaseClass
from .windowseventlog import WindowsEventLog
from .sysmon import SysMon


class ElasticECS(BaseClass):

    """Generate Elastic Common Schema document to push to elastic
    
    Example Usage:

      import pprint
      doc = ElasticECS()
      print(doc.get())
    """

    _version = "1.5.0"
    __fields = None

    def __init__(self, sysmon=False, windows_events=False):
        super(ElasticECS, self).__init__()
        if windows_events:
            self.win_events = WindowsEventLog(json=True)
        elif sysmon:
            pass
            # self.sysmon_events = SysMon().get(count=1)

    @property
    def fields(self):
        if not self.__fields:
            from .elasticecsfields import ElasticECSFields
            self.__fields = ElasticECSFields()
        return self.__fields

    def get(self, count=1):
        """Generates one or more Elastic Common Schema documents

        Args:
            count (int, optional): The number of documents you want 
                                   generated. Defaults to 1.

        Returns:
            list: A list of ECS Document dictionaries
        """
        ecs_list = []
        for event in self.win_events.get(count=count):
            event_data_dict = {}
            if event['Event'].get('EventData'):
                for key,val in event['Event']['EventData'].items():
                    event_data_dict.update({
                      key:val
                    })
                self.__hidden_event = None
                self.__hidden_event = event
                _document = None
                _document = self.fields.base
                _document = {
                    'agent': self.fields.agent,
                    'client': self.fields.client,
                    'cloud': self.fields.cloud,
                    'code_signature': self.fields.code_signature,
                    'container': self.fields.container,
                    'destination': self.fields.destination,
                    'dll': self.fields.dll,
                    'dns': self.fields.dns,
                    'ecs': {
                        'version': self._version
                    },
                    'event': self.fields.event,
                    'file': self.fields.file,
                    'host': self.fields.host,
                    'http': self.fields.http,
                    'network': self.fields.network,
                    'organization': self.fields.organization,
                    'package': self.fields.package,
                    'registry': self.fields.registry,
                    'server': self.fields.server,
                    'source': self.fields.source
                }
                ecs_list.append(_document)
        return ecs_list
