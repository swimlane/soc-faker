class Logs(object):

    """The main entry point to generate different log standards
    """

    def syslog(self, type='ransomware', count=10):
        """The syslog method generates random syslog messages based on the type and count requested

        Args:
            type (str, optional): Generates random syslog files with ransomware traffic added randomly. Defaults to 'ransomware'.
            count (int, optional): The number of logs to generate. Defaults to 10.

        Returns:
            list: Returns a list of generated syslogs
        """
        from .logstreamer import LogStreamer
        return LogStreamer().generate(type=type, count=count)

    @property
    def windows(self):
        """The windows property gives you access to logs related to windows operating systems

        Returns:
            Windows: Returns a Windows object containing properties for different log types and formats
        """
        from .windows import Windows
        return Windows()
