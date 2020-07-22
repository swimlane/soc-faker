class Windows(object):

    """The Windows class gives the user access to logs and other data related to Windows
    """
    def eventlog(self, count=1, computer_name=None, os_version='Windows', json=False):
        """Generate fake event logs based on the provided inputs

        Args:
            count (int, optional): The number of logs to generate. Defaults to 1.
            computer_name (str, optional): A computer name to use when generating logs. Defaults to None.
            os_version (str, optional): The Operating System version to use when generating logs. Defaults to 'Windows'.
            json (bool, optional): Whether or not to return data as JSON or XML. Defaults to False.

        Returns:
            list: Returns a list of generated Windows Event Logs
        """
        from .windowseventlog import WindowsEventLog
        return WindowsEventLog(json=json).get(count=count, computer_name=computer_name, os_version=os_version)

    def sysmon(self, count=1):
        """Generate fake sysmon logs for Windows

        Args:
            count (int, optional): The number of logs to generate. Defaults to 21.

        Returns:
            list: Returns a list of generated SysMon logs
        """
        from .sysmon import SysMon
        return SysMon().get(count=count)
