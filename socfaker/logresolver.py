import weakref


class LogResolver(object):
    """Provides automatic weakref resolution for Swimlane client to avoid circular references and memory leaks"""

    def __init__(self, logs):
        self.__ref_logs = weakref.ref(logs)

    @property
    def _logs(self):
        """Transparently resolve the swimlane weakref"""
        return self.__ref_logs()
