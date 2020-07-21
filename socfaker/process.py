from .network import Network
from .computer import Computer
from .timestamp import Timestamp
from .baseclass import BaseClass


class Process(BaseClass):

    """The Process class contains properties about a process on a system

    Returns:
        Process: An object with properties common to Processes
    """

    _agent_id = None

    def __init__(self, windows_event_obj=None, sysmon_event_obj=None):
        if windows_event_obj:
            self.args = self.__search_dict(windows_event_obj, 'process')
        elif sysmon_event_obj:
            pass

    def __search_dict(self, search_dict, field):
        """
        Takes a dict with nested lists and dicts,
        and searches all dicts for a key of the field
        provided.
        """
        fields_found = []
        for key, value in search_dict.iteritems():
            if field in key:
                fields_found.append(value)
            elif isinstance(value, dict):
                results = self.__search_dict(value, field)
                for result in results:
                    fields_found.append(result)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        more_results = self.__search_dict(item, field)
                        for another_result in more_results:
                            fields_found.append(another_result)
        return fields_found

    @property
    def args(self):
        if not self._args:
            # then we need to generate args
            pass
        return self._args

    @args.setter
    def args(self, value):
        if value:
            self._args = value
        else:
            self._args = []

    @property
    def args_count(self):
        return len(self.args)
    
    @property
    def command_line(self):
        return ''.join(x for x in self.args)

    @property
    def entity_id(self):
        return str(self.uuid.uuid4())
    
    @property
    def executable(self):
        return self.args[0]
    
    @property
    def name(self):
        pass

    @property
    def parent(self):
        return Process()

    @property
    def pid(self):
        return self.random.randint(0,9999)

    @property
    def start(self):
        return Timestamp().current

    @property
    def thread_id(self):
        return self.pid
