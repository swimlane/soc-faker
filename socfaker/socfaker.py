
class SocFaker(object):


    @property
    def application(self):
        from .application import Application
        return Application()

    @property
    def computer(self):
        from .computer import Computer
        return Computer()

    @property
    def employee(self):
        from .employee import Employee
        return Employee()

    @property
    def file(self):
        from .file import File
        return File()

    @property
    def logs(self):
        from .logs import Logs
        return Logs()

    @property
    def network(self):
        from .network import Network
        return Network()

    @property
    def organization(self):
        from .organization import Organization
        return Organization()

    @property
    def products(self):
        from .products import Products
        return Products()

    @property
    def user_agent(self):
        from .useragent import UserAgent
        return UserAgent().get()
    
    
    def vulnerability(self, host_count=1, critical=1, high=1, medium=1, low=1, informational=1):
        from .vulnerability import Vulnerability
        return Vulnerability(host_count=host_count,critical=critical,high=high,medium=medium,low=low,informational=informational)