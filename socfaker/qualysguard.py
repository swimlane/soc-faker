from string import digits
from .employee import Employee
from .baseclass import BaseClass
from .timestamp import Timestamp


class QualysGuard(BaseClass):
    """The QualysGuard Class has a method to retrieve information about a QualysGuard Vulnerability Management scan
    """

    def scan(self, count=1, host_count=1):
        """Retrieve 1 or more QualysGuard VM scans for 1 or more hosts

        Args:
            count (int, optional): The number of scans to return. Defaults to 1.
            host_count (int, optional): The number of hosts within a scan. Defaults to 1.

        Returns:
            list: Returns a list of scans based on the provided inputs
        """
        sc = 0
        return_list = []
        while sc < count:
            employee = Employee()
            hosts = self.__get_scanned_hosts(host_count=host_count)
            return_list.append({
                'scan_report_template_title': "Scan Results {}".format(self.random.randint(1, 5000)),
                'result_date': Timestamp().in_the_past(),
                'name': '{} {}'.format(employee.first_name, employee.last_name),
                'username': employee.username,
                'role': employee.title,
                'scan_date': Timestamp().in_the_past(),
                'total_hosts': len(hosts),
                'type': self.random.choice(['On-Demand', 'Scheduled','API']),
                'status': self.random.choice(['Finished', 'Canceled', 'Paused', 'Error']),
                'reference': "scan/" + ''.join(self.random.choice(digits) for i in range(10)) + '.' + ''.join(self.random.choice(digits) for i in range(5)),
                'duration': "{}:{}:{}".format(self.random.randint(0, 59), self.random.randint(0, 59), self.random.randint(0, 59)),
                'scan_title': "My Scan {}".format(self.random.randint(1, 25)),
                'ips': hosts
            })
            sc += 1
        return return_list

    def __get_scanned_hosts(self, host_count=1):
        if host_count < 256:
            ip = [10,10,0,0]
            ip_list = []
            for i in range(host_count):
                ip_list.append("{}.{}.{}.{}".format(ip[0], ip[1], ip[2], ip[3] + i))
        return ip_list
