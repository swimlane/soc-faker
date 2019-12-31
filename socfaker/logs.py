class Logs(object):

    def syslog(self, type='ransomware', count=10):
        from .logstreamer import LogStreamer
        return LogStreamer().generate(type=type, count=count)

    @property
    def windows(self):
        from .windows import Windows
        return Windows()
