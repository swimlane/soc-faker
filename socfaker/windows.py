

class Windows(object):

    def eventlog(self, count=1, computer_name=None, os_version='Windows', file_directory='./data/windows-events/', json=False):
        from .windowseventlog import WindowsEventLog
        return WindowsEventLog(file_directory=file_directory, json=json).get(count=count, computer_name=computer_name, os_version=os_version)

    def sysmon(self, count=21):
        from .sysmon import SysMon
        return SysMon().get(count=count)
        
