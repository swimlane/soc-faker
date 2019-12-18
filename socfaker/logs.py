class Logs(object):

    def syslog(self, type='ransomware'):
        from .logstreamer import LogStreamer
        return LogStreamer().generate(type=type)

    @property
    def windows(self):
        from .windows import Windows
        return Windows()
