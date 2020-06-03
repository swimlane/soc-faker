class Logs(object):

    def syslog(self, type='ransomware', count=10):
        from .logstreamer import LogStreamer
        return LogStreamer().generate(type=type, count=count)

    def access(self, type='test', count=10, path_file='', clients=0):
        from .accesslogstreamer import AccessLogStreamer
        return AccessLogStreamer().generate(type=type, count=count, path_file=path_file, clients=clients)

    @property
    def windows(self):
        from .windows import Windows
        return Windows()

