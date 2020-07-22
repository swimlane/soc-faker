import base64
from .timestamp import Timestamp
from .alert import Alert
from .organization import Organization
from .agent import Agent
from .cloud import Cloud
from .file import File
from .registry import Registry
from .computer import Computer
from .container import Container
from .location import Location
from .network import Network
from .dns import DNS
from .http import HTTP
from .application import Application
from .operatingsystem import OperatingSystem
from .baseclass import BaseClass


class ElasticECSFields(BaseClass):

    """The ElasticECSFields class contains defined properties 
       based on the ECS specification.

       You can access these directly via the 
       products.elastic.document.fields property path
       or generate an entire document based on these 
       properties using
       products.elastic.document.get()
    """

    def __init__(self):
        super(ElasticECSFields, self).__init__()
        self.__app = Application()
        self.__http_class = HTTP()
        self.__operating_system = OperatingSystem()
        self.__organization = Organization()
        self.__computer = Computer()
        self.__dns = DNS()
        self.__container = Container()
        self.__file = File()
        self.__cloud = Cloud()
        self.__agent = Agent()
        self.__alert = Alert()
        self.__time = Timestamp()

    def __get_geo_data(self):
        loc = Location()
        return {
            'city_name': loc.city,
            'continent_name': loc.continent,
            'country_iso_code': loc.country_code,
            'country_name': loc.country,
            'location': {
                'lon': loc.longitude,
                'lat': loc.latitude
            }
        }

    def __get_file_code_signature(self):
        return {
            'exists': self.random.choice([True, False]),
            'status': self.__file.signature_status,
            'subject_name': self.__file.signature,
            'trusted': self.random.choice([True, False]),
            'valid': self.random.choice([True, False])
        }

    def __get_file_hash(self):
        return self.__file.hashes
    
    def __get_file_pe(self):
        return {
            'company': 'Microsoft Corporation',
            'description': self.__file.name,
            'file_version': self.__file.version,
            'original_file_name': self.__file.name
        }
        
    @property
    def agent(self):
        """Returns an ECS agent dictionary

        Returns:
            dict: Returns a dictionary of agent
                  fields/properties
        """
        return {
            'ephemeral_id': self.__agent.ephermeral_id,
            'id': self.__agent.id,
            'name': self.__agent.name,
            'type': self.__agent.type,
            'version': self.__agent.version
        }

    @property
    def base(self):
        """Returns an ECS base fields dictionary

        Returns:
            dict: Returns a dictionary of ECS base
                  fields/properties
        """
        return {
            '@timestamp': self.__time.in_the_past(),
            'lables': {'type': self.__alert.type, 'status': self.__alert.status},
            'message': self.__alert.summary,
            'tags': [self.__alert.type]
        }

    @property
    def client(self):
        """Returns an ECS Client dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  client fields/properties
        """
        comp = Computer()
        network = Network(private=True)
        ip = network.ipv4
        return {
            "address": ip,
            "domain": Organization().domain,
            "ip": ip,
            "mac": comp.mac_address,
            "port": network.port.values(),
            "nat": {
                "ip": Network(private=True).ipv4,
                "port": network.port.values()
            },
            "packets": self.random.randint(7,2160),
            "bytes": self.random.randint(120,10160),
            "geo": self.__get_geo_data()
        }
    
    @property
    def container(self):
        """Returns an ECS container dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  container fields/properties
        """
        return {
            'id': self.__container.id,
            'image': {
                'name': self.__container.name,
                'tag': self.__container.tags
            },
            'name': self.__container.name,
            'runtime': self.__container.runtime
        }

    @property
    def destination(self):
        """Returns an ECS destination dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  destination fields/properties
        """
        comp = Computer()
        network = Network(private=False)
        ip = network.ipv4
        return {
            "address": ip,
            "domain": Organization().domain,
            "ip": ip,
            "mac": comp.mac_address,
            "port": network.port.values(),
            "nat": {
                "ip": Network(private=True).ipv4,
                "port": network.port.values()
            },
            "packets": self.random.randint(7,2160),
            "bytes": self.random.randint(120,10160),
            "geo": self.__get_geo_data()
        }

    @property
    def dll(self):
        """Returns an ECS DLL dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  DLL fields/properties
        """
        return {
            'name': self.__file.name,
            'path': self.__file.full_path,
            'code_signature': self.__get_file_code_signature(),
            'hash': self.__get_file_hash(),
            'pe': self.__get_file_pe()
        }

    @property
    def dns(self):
        """Returns an ECS DNS dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  DNS fields/properties
        """
        return {
            'answers': self.__dns.answers,
            'header_flags': self.__dns.header_flags,
            'id': self.__dns.id,
            'op_code': self.__dns.op_code,
            'question': self.__dns.question,
            'response_code': self.__dns.response_code   
        }

    @property
    def event(self):
        """Returns an ECS Event dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  Event fields/properties
        """
        if hasattr(self, '__hidden_event'):
            return {
                'action': '{}-{}-{}'.format(self.random.choice(['process', 'file', 'user']), self.random.choice(['password', 'ran', 'stopped']), self.random.choice(['started', 'created', 'deleted'])),
                'category': self.random.choice(['authentication', 'database', 'driver', 'file', 'host', 'iam', 'intrusion_detection', 'malware', 'network', 'package', 'process', 'web']),
                'code': self.__hidden_event.get('Event').get('System').get('EventId'),
                'created': self.__hidden_event.get('Event').get('System').get('TimeCreated').get('@SystemTime'),
                'dataset': 'windows.{}'.format(self.random.choice(['authentication', 'database', 'driver', 'file', 'host', 'iam', 'intrusion_detection', 'malware', 'network', 'package', 'process', 'web'])),
                'id': self.__hidden_event.get('Event').get('System').get('Provider').get('@Guid'),
                'kind': self.random.choice(['alert', 'event', 'metric', 'state', 'pipeline_error', 'signal']),
                'module': 'windows',
                'original': str(self.__hidden_event),
                'outcome': self.random.choice(['failure', 'unknown'] + ['success'] * 4),
                'provider': self.__hidden_event.get('Event').get('System').get('Provider'),
                'risk_socre': self.random.randint(1,100),
                'risk_score_norm': self.random.randint(1,100),
                'severity': int(self.__hidden_event.get('Event').get('System').get('Level')),
                'start': self.__hidden_event.get('Event').get('System').get('TimeCreated').get('@SystemTime'),
                'type': [self.random.choice(['access', 'admin', 'allowed', 'change', 'connection', 'creation', 'deletion', 'denied', 'end', 'error', 'group', 'info', 'installation', 'protocol', 'start', 'user']) for x in range(self.random.randint(1,5))],
            }
        else:
            return {
                'action': '{}-{}-{}'.format(self.random.choice(['process', 'file', 'user']), self.random.choice(['password', 'ran', 'stopped']), self.random.choice(['started', 'created', 'deleted'])),
                'category': self.random.choice(['authentication', 'database', 'driver', 'file', 'host', 'iam', 'intrusion_detection', 'malware', 'network', 'package', 'process', 'web']),
                'code': self.random.randint(1,9999),
                'created': self.__time.in_the_past(),
                'dataset': 'windows.{}'.format(self.random.choice(['authentication', 'database', 'driver', 'file', 'host', 'iam', 'intrusion_detection', 'malware', 'network', 'package', 'process', 'web'])),
                'id': str(self.uuid.uuid4()),
                'kind': self.random.choice(['alert', 'event', 'metric', 'state', 'pipeline_error', 'signal']),
                'module': 'windows',
                'outcome': self.random.choice(['failure', 'unknown'] + ['success'] * 4),
                'provider': 'Windows',
                'risk_socre': self.random.randint(1,100),
                'risk_score_norm': self.random.randint(1,100),
                'severity': self.random.randint(1,7),
                'start': self.__time.in_the_past(),
                'type': [self.random.choice(['access', 'admin', 'allowed', 'change', 'connection', 'creation', 'deletion', 'denied', 'end', 'error', 'group', 'info', 'installation', 'protocol', 'start', 'user']) for x in range(self.random.randint(1,5))],
            }
        
    @property
    def file(self):
        """Returns an ECS file dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  file fields/properties
        """
        return {
            'accessed': self.__file.accessed_timestamp,
            'attributes': self.__file.attributes,
            'created': self.__file.timestamp,
            'ctime': self.__file.timestamp,
            'directory': self.__file.directory,
            'drive_letter': self.__file.drive_letter,
            'extension': self.__file.extension,
            'gid': self.__file.gid,
            'mime_type': self.__file.mime_type,
            'name': self.__file.name,
            'path': self.__file.full_path,
            'size': self.__file.size,
            'type': self.__file.type,
            'code_signature': self.__get_file_code_signature(),
            'hash': self.__get_file_hash(),
            'pe': self.__get_file_pe()
        }

    @property
    def host(self):
        """Returns an ECS host dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  host fields/properties
        """
        network = Network(private=True)
        ip = network.ipv4
        return {
            'architecture': self.__computer.architecture,
            'domain': self.__organization.domain,
            'hostname': self.__computer.name.replace('-', '_'),
            'id': str(self.uuid.uuid4()),
            'ip': [ip],
            'mac': self.__computer.mac_address,
            'name': self.__computer.name.replace('-', '_'),
            'type': self.__computer.platform,
            'geo': self.__get_geo_data(),
            'os': {
                'family': self.__operating_system.family,
                'full': self.__operating_system.fullname,
                'name': self.__operating_system.name,
                'platform': self.__computer.platform,
                'version': self.__operating_system.version
            }
        }

    @property
    def http(self):
        """Returns an ECS HTTP dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  HTTP fields/properties
        """
        return {
            'request': self.__http_class.request,
            'response': self.__http_class.response
        }

    @property
    def network(self):
        """Returns an ECS network dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  network fields/properties
        """
        protocol = Network().protocol
        return {
            'application': self.__app.name,
            #'bytes': # Need to add source.bytes and destination.bytes to get ths value
            'direction': self.__dns.direction,
            'forwaded_ip': self.host['ip'],
            'type': self.random.choice(['ipv4', 'ipv6', 'ipsec', 'pim']),
            'protocol': protocol.values(),
            'transport': protocol.keys()
        }

        

    @property
    def organization(self):
        """Returns an ECS Organization dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  organization fields/properties
        """
        return {
            'id': str(self.uuid.uuid4()),
            'name': self.__organization.name
        }

    @property
    def package(self):
        """Returns an ECS package dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  package fields/properties
        """
        return {
            'architecture': self.__computer.architecture,
            'build_version': self.__file.build_version,
            'checksum': self.__file.checksum,
            'install_scope': self.__file.install_scope,
            'installed': self.__file.timestamp,
            'name': self.__file.name,
            'path': self.__file.full_path,
            'size': self.__file.size,
            'version': self.__file.version
        }

    @property
    def registry(self):
        """Returns an ECS Windows Registry dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  Windows Registry fields/properties
        """
        reg = Registry()
        value = reg.value
        return {
            'data': {
                'bytes': base64.b64encode(str(value).encode()),
                'strings': [value],
                'type': reg.type
            },
            'hive': reg.hive,
            'key': reg.key,
            'path': reg.path,
            'value': value
        }

    @property
    def server(self):
        """Returns an ECS server dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  server fields/properties
        """
        net = Network()
        address = net.ipv4
        return {
            'address': address,
            'bytes': self.random.randint(1,420),
            'ip': address,
            'mac': Computer().mac_address,
            'packets': self.random.randint(1,80),
            'port': net.port.values(),
            'geo': self.__get_geo_data()
        }

    @property
    def source(self):
        """Returns an ECS source dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  source fields/properties
        """
        comp = Computer()
        network = Network(private=True)
        ip = network.ipv4
        return {
            "address": ip,
            "domain": Organization().domain,
            "ip": ip,
            "mac": comp.mac_address,
            "port": network.port.values(),
            "nat": {
                "ip": Network(private=True).ipv4,
                "port": network.port.values()
            },
            "packets": self.random.randint(7,2160),
            "bytes": self.random.randint(120,10160),
            "geo": self.__get_geo_data()
        }

    @property
    def cloud(self):
        """Returns an ECS Cloud dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  Cloud fields/properties
        """
        return {
            'account': {
                'id': self.__cloud.id
            },
            'availability_zone': self.__cloud.zone,
            'instance': {
                'id': self.__cloud.instance_id,
                'name': self.__cloud.name
            },
            'machine': {
                'type': self.__cloud.name
            },
            'provider': self.__cloud.provider,
            'region': self.__cloud.region
        }

    @property
    def code_signature(self):
        """Returns an ECS Code Signature dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  Code Signature fields/properties
        """
        return {
            'exists': self.random.choice([True, False]),
            'status': self.__file.signature_status,
            'subject_name': self.__file.signature,
            'trusted': self.random.choice([True, False]),
            'valid': self.random.choice([True, False])
        }
