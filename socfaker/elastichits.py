import string
from .windowseventlog import WindowsEventLog
from .computer import Computer
from .baseclass import BaseClass


class ElasticHits(BaseClass):

    """Fake's Elastic Search Hits from Windows Event Data
    
    Example Usage:

      hits = ElasticHits()
      print(hits.get(count=15))

    """    
    
    def __init__(self):
        """ElasticHits uses Windows Event Logs to generate fake response to queries to elasticsearch
        """
        super(ElasticHits, self).__init__()
        self.win_events = WindowsEventLog(json=True)
        self.host_id = str(self.uuid.uuid4())
        self.__computer = Computer()

    def get(self, count=10):
        """The get method is the main method to retrieve a specified count (default of 10) 
        of Elasticsearch hits

        Args:
            count (int, optional): The number of hits to return. Defaults to 10.

        Returns:
            list: Returns a list of elasticsearch query hits
        """
        self.count = count
        hit_list = self._get_hits()
        return {
            "total": len(hit_list),
            "max_score": 'null',
            "hits": hit_list
        }

    def _get_hits(self):
        hit_list = []
        count = 0
        for event in self.win_events.get(computer_name=self.__computer.name):
            while count <= self.count:
                event_data_dict = {}
                if event['Event'].get('EventData'):
                    for key,val in event['Event']['EventData'].items():
                        event_data_dict.update({
                          key:val
                        })
                    hit_dict = {
                        '_index': 'winlogbeat-7.2.0-2019.06.27-000001',
                        '_type': '_doc',
                        '_id': '{}-{}'.format(self._random_id(9), self._random_id(10)),
                        '_version': 1,
                        '_score': 'null',
                        '_source': {
                            '@timestamp': event['Event']['System']['TimeCreated']['@SystemTime'],
                            'log': {
                                'level': '{}'.format(self.get_log_level(event['Event']['System']['Level']))
                            },
                            'process': {
                                'pid': event['Event']['System']['Execution']['@ProcessID'],
                                "executable": '-' if not event['Event']['EventData'].get('NewProcessName') else event['Event']['EventData']['NewProcessName'],
                                "name": '-' if not event['Event']['EventData'].get('NewProcessName') else event['Event']['EventData']['NewProcessName']
                            },
                            "host": {
                                "id": self.host_id,
                                "hostname": self.__computer.name,
                                "architecture": "x86_64",
                                "name": self.__computer.name,
                                "os": {
                                    "platform": self.__computer.platform,
                                    "version": "10.0",
                                    "family": "windows",
                                    "name": self.__computer.os,
                                    "kernel": "10.0.17763.379 (WinBuild.160101.0800)",
                                    "build": "17763.379"
                                }
                            },
                            "agent": {
                                "hostname": self.__computer.name,
                                "id": self.host_id,
                                "version": "7.2.0",
                                "type": "winlogbeat",
                                "ephemeral_id": "08aa7e91-b37f-48c3-a058-7022f24856dd"
                            },
                            "winlog": {
                                "record_id": event['Event']['System']['EventRecordID'],
                                "opcode": event['Event']['System']['Level'],
                                "version": event['Event']['System']['Version'],
                                "channel": event['Event']['System']['Provider']['@Name'],
                                "process": {
                                  "pid": event['Event']['System']['Execution']['@ProcessID'],
                                  "thread": {
                                    "id": event['Event']['System']['Execution']['@ThreadID']
                                  }
                                },
                                "task": event['Event']['System']['Task'],
                                "keywords": [
                                  "Audit Success"
                                ],
                                "provider_guid": event['Event']['System']['Provider']['@Guid'],
                                "provider_name": event['Event']['System']['Provider']['@Name'],
                                "api": "wineventlog",
                                "computer_name": "{}.deepdive.local".format(self.__computer.name),
                                "event_data": event_data_dict,
                                "event_id": event['Event']['System']['EventId']
                            },
                        }
                    }
                    hit_list.append(hit_dict)
                    count += 1
        return hit_list

    def get_log_level(self, value):
        if value == '0':
            return 'Trace'
        if value == '1':
            return 'Debug'
        if value == '2':
            return 'Informational'
        if value == '3':
            return 'Warning' 
        if value == '4':
            return 'Error'
        if value == '5':
            return 'Critical'
        if value == '6':
            return 'None'

    def _random_id(self, stringLength):
        lettersAndDigits = string.ascii_letters + string.digits
        return ''.join(self.random.choice(lettersAndDigits) for i in range(stringLength))
