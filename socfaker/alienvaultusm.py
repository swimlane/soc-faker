from .baseclass import BaseClass
from .alert import Alert
from .network import Network
from .dns import DNS
from .location import Location


class AlienVaultUSM(BaseClass):

    def __init__(self):
        super(AlienVaultUSM, self).__init__()
        self.__alert = Alert()
        self.__priv_network = Network(private=True)
        self.__pub_network = Network()
        self.__dns = DNS()
        self.__dest_location = Location()
        self.__source_location = Location()

    @property
    def event_type(self):
        return self.__alert.type

    @property
    def id(self):
        return str(self.uuid.uuid4())

    @property
    def description(self):
        return 'This is an example event description from soc-faker'
    
    @property
    def severity(self):
        return self.__alert.severity_label

    @property
    def action(self):
        return self.__alert.action
 
    @property
    def category(self):
        return self.random.choice(['Recon', 'Security'])

    @property
    def subcategory(self):
        return self.random.choice(['Microsoft-Windows-Security-Auditing', 'Scanner'])

    @property
    def destination_hostname(self):
        return self.__priv_network.hostname

    @property
    def destination_fqdn(self):
        return self.__dns.name

    @property
    def destination_address(self):
        return self.__priv_network.ipv4

    @property
    def destination_port(self):
        if not hasattr(self, '__priv_port'):
            self.__priv_port = self.__priv_network.port
        return list(self.__priv_port.keys())[0]

    @property
    def destination_port_label(self):
        if not hasattr(self, '__priv_port'):
            self.__priv_port = self.__priv_network.port
        return list(self.__priv_port.values())[0]
        
    @property
    def destination_asset_id(self):
        return str(self.uuid.uuid4())
    
    @property
    def destination_longitude(self):
        return self.__dest_location.longitude
    
    @property
    def destination_latitude(self):
        return self.__dest_location.latitude

    @property
    def destination_city(self):
        return self.__dest_location.city
    
    @property
    def destination_country(self):
        return self.__dest_location.country

    @property
    def destination_region(self):
        return self.__dest_location.continent

    @property
    def source_hostname(self):
        return self.__pub_network.hostname

    @property
    def source_fqdn(self):
        return self.__dns.name

    @property
    def source_address(self):
        return self.__pub_network.ipv4

    @property
    def source_port(self):
        if not hasattr(self, '__pub_port'):
            self.__pub_port = self.__pub_network.port
        return list(self.__pub_port.keys())[0]

    @property
    def source_port_label(self):
        if not hasattr(self, '__pub_port'):
            self.__pub_port = self.__pub_network.port
        return list(self.__pub_port.values())[0]

    @property
    def source_asset_id(self):
        return str(self.uuid.uuid4())
    
    @property
    def source_longitude(self):
        return self.__source_location.longitude
    
    @property
    def source_latitude(self):
        return self.__source_location.latitude

    @property
    def source_city(self):
        return self.__source_location.city
    
    @property
    def source_country(self):
        return self.__source_location.country

    @property
    def source_region(self):
        return self.__source_location.continent

    @property
    def plugin(self):
        return self.random.choice(['Amazon AWS CloudTrail', 'AlienVault Agent - Windows EventLog', 'AlienVault NIDS'])
        
    @property
    def plugin_device(self):
        return self.random.choice(['CloudTrail', 'AlienVault Agent', 'AlienVault NIDS'])
    
    @property
    def plugin_device_type(self):
        return self.random.choice(['Cloud Infrastructure', 'Intrusion Detection', 'Endpoint Security'])

    @property
    def plugin_version(self):
        return self.random.choice(['0.50', '0.43', '0.14'])
    
    @property
    def packets_sent(self):
        return self.random.randint(7,2160)
    
    @property
    def packets_received(self):
        return self.random.randint(7,2160)
    
    @property
    def packet_type(self):
        return self.random.choice(['log'])
    
    @property
    def bytes_in(self):
        from .http import HTTP
        return HTTP().bytes
        
    @property
    def bytes_out(self):
        from .http import HTTP
        return HTTP().bytes

    @property
    def app_display_name(self):
        from .application import Application
        return Application().name
    
    @property
    def application_protocol(self):
        if not hasattr(self, '__priv_protocol'):
            self.__priv_protocol = self.__priv_network.protocol
        return list(self.__priv_protocol.keys())[0]
        
    @property
    def transport_protocol(self):
        if not hasattr(self, '__priv_protocol'):
            self.__priv_protocol = self.__priv_network.protocol
        return list(self.__priv_protocol.values())[0]
