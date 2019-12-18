import random, pendulum
from string import digits

from .employee import Employee


class QualysGuard(object):

    def scan(self, count=1, host_count=1):
        sc = 0
        return_list = []
        while sc < count:
            employee = Employee()
            hosts = self.__get_scanned_hosts(host_count=host_count)
            return_list.append({
              'scan_report_template_title': "Scan Results {}".format(random.randint(1, 5000)),
              'result_date': pendulum.now().subtract(days=random.randint(1,30), hours=random.randint(1,59), minutes=random.randint(1,59), seconds=random.randint(1,59)),
              'name': '{} {}'.format(employee.first_name, employee.last_name),
              'username': employee.username,
              'role': employee.title,
              'scan_date': pendulum.now().subtract(days=random.randint(1,30), hours=random.randint(1,59), minutes=random.randint(1,59), seconds=random.randint(1,59)),
              'total_hosts': len(hosts),
              'type': random.choice(['On-Demand', 'Scheduled','API']),
              'status': random.choice(['Finished', 'Canceled', 'Paused', 'Error']),
              'reference': "scan/" + ''.join(random.choice(digits) for i in range(10)) + '.' + ''.join(random.choice(digits) for i in range(5)),
              'duration': "{}:{}:{}".format(random.randint(0, 59), random.randint(0, 59), random.randint(0, 59)),
              'scan_title': "My Scan {}".format(random.randint(1, 25)),
              'ips': hosts
            })
            sc += 1
        return return_list

    def __get_scanned_hosts(self, host_count=1):
        if host_count < 256:
            ip = [10,10,0,0]
            ip_list = []
            for i in range(host_count):
                ip_list.append("%s.%s.%s.%s" % (ip[0], ip[1], ip[2], ip[3] + i))
        return ip_list
        


# TODO: Add Additional Scan Specific Details
# 
'''
{
    'protocol': 
}

"protocol": {
      "name": "Protocol"
    },
    "LAST_SERVICE_MODIFICATION_DATETIME": {
      "name": "Last Service Modification Datetime"
    },
    "qid": {
      "name": "Qid"
    },
    "VULN_TYPE": {
      "name": "Vuln Type"
    },
    "result": {
      "name": "Result"
    },
    "port": {
      "name": "Port"
    },
    "DISCOVERY": {
      "name": "Discovery"
    },
    "SEVERITY_LEVEL": {
      "name": "Severity Level"
    },
    "QID": {
      "name": "Qid"
    },
    "TITLE": {
      "name": "Title"
    },
    "PCI_FLAG": {
      "name": "Pci Flag"
    },
    "dns": {
      "name": "Dns"
    },
    "ip": {
      "name": "Ip"
    },
    "PUBLISHED_DATETIME": {
      "name": "Published Datetime"
    },
    "ssl": {
      "name": "Ssl"
    },
    "DIAGNOSIS": {
      "name": "Diagnosis"
    },
    "CONSEQUENCE": {
      "name": "Consequence"
    },
    "netbios": {
      "name": "Netbios"
    },
    "CATEGORY": {
      "name": "Category"
    },
    "fqdn": {
      "name": "Fqdn"
    },
    "composite_key": {
      "name": "Composite Key"
    },
    "PATCHABLE": {
      "name": "Patchable"
    }
  },
'''