import glob, os, fnmatch
from string import Formatter
from .computer import Computer
from .file import File
from .organization import Organization
from .employee import Employee
from .network import Network
from .registry import Registry
from .timestamp import Timestamp
from .baseclass import BaseClass


class SysMon(BaseClass):

    """The SysMon class will generate fake sysmon logs for Microsoft Windows operating systems

    Returns:
        SysMon: Returns an object containing a get method to retrieve generated sysmon logs
    """

    __DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'sysmon'))

    def __init__(self):
        super(SysMon, self).__init__()
        self.templates = self.__check_file_directory()

    def get(self, count=1):
        """Returns a list of generated sysmon logs

        Args:
            count (int, optional): The number of sysmon logs to return. Defaults to 21.

        Returns:
            list: A list of generated sysmon logs
        """
        return_list = []
        current_count = 1
        
        shuffled = self.random.sample(self.templates, len(self.templates))
        for template in shuffled:
            while current_count <= count:
                current_count += 1
                with open(template, 'r') as file:
                    data = file.read()
                names = [fn for _, fn, _, _ in Formatter().parse(data) if fn is not None]
                computer = Computer()
                f = File()
                org = Organization()
                emp = Employee()
                net = Network()
                properties = {}
                for item in names:
                    if item == 'guid':
                        properties['guid'] = str(self.uuid.uuid4())
                    elif item == 'timestamp':
                        properties['timestamp'] = Timestamp().in_the_future(days=self.random.randint(1,15), hours=self.random.randint(1,24), minutes=self.random.randint(1,60), seconds=self.random.randint(1,60))
                    elif item == 'creation_time':
                        properties['creation_time'] = Timestamp().in_the_past(days=self.random.randint(1,15), hours=self.random.randint(1,24), minutes=self.random.randint(1,60), seconds=self.random.randint(1,60))
                    elif item == 'previous_creation_time':
                        properties['previous_creation_time'] = properties['timestamp']
                    elif item == 'process_id':
                        properties['process_id'] = self.random.randint(2000,4000)
                    elif item == 'thread_id':
                        properties['thread_id'] = self.random.randint(2000,4000)
                    elif item == 'image_path':
                        f = File()
                        properties['image_path'] = '{}\\{}'.format(f.full_path, f.name)
                    elif item == 'current_directory':
                        properties['current_directory'] = '{}'.format(f.full_path)
                    elif item == 'parent_path':
                        properties['parent_path'] = '{}'.format(f.full_path)
                    elif item == 'process_state':
                        properties['process_state'] = 'Loaded'
                    elif item == 'computer_name':
                        properties['computer_name'] = computer.name
                    elif item == 'domain':
                        properties['domain'] = org.domain
                    elif item == 'user':
                        properties['user'] = emp.username
                    elif item == 'protocol':
                        properties['protocol'] = net.protocol
                    elif item == 'source_ip':
                        properties['source_ip'] = Network(private=True).ipv4
                    elif item == 'source_port':
                        properties['source_port'] = self.random.randint(100,5000)
                    elif item == 'destination_ip':
                        properties['destination_ip'] = net.ipv4
                    elif item == 'destination_port':
                        properties['destination_port'] = self.random.randint(100,5000)
                    elif item == 'target_filename':
                        properties['target_filename'] = f.name
                    elif item == 'registry_object':
                        properties['registry_object'] = '{}'.format(Registry().key)
                    elif item == 'registry_value':
                        properties['registry_value'] = properties['registry_object'].split('\\',1)[1]
                    elif item == 'exe':
                        properties['exe'] = f.name
                    elif item == 'sha1':
                        properties['sha1'] = f.sha1
                    elif item == 'sha256':
                        properties['sha256'] = f.sha256
                    elif item == 'signed':
                        properties['signed'] = f.signed
                    elif item == 'signature':
                        properties['signature'] = f.signature
                    elif item == 'signature_status':
                        properties['signature_status'] = f.signature_status
                    elif item == 'integrity_level':
                        properties['integrity_level'] = self.random.choice(['Low', 'Medium', 'High'])
                return_list.append(data.format(**properties))
        return return_list

    def __check_file_directory(self):
        matches = []
        for root, dirnames, filenames in os.walk(self.__DATA_PATH):
            for filename in fnmatch.filter(filenames, '*.txt'):
                matches.append(os.path.abspath(os.path.join(root, filename)))
        return matches