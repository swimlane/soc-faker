
class Products(object):

    @property
    def azure(self):
        from .azure import Azure
        return Azure()

    @property
    def elastic(self):
        from .elastic import Elastic
        return Elastic()

    @property
    def servicenow(self):
        from .servicenow import ServiceNow
        return ServiceNow()

    @property
    def qualysguard(self):
        from .qualysguard import QualysGuard
        return QualysGuard()