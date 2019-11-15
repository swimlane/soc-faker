import random
from logresolver import LogResolver
from ransomware import Ransomware


class LogAdapter(LogResolver):


    def _get_infected_list(self, count):
        self.infected_list = random.sample(self._logs.internal_ip_list, count)
        for item in self.infected_list:
            self._logs.internal_ip_list.remove(item)
        self.clean_list = self._logs.internal_ip_list

    def _get_external_paths(self):
        self.external_paths = []
        for _ in range(random.randint(1, 20)):
            self.external_paths.append(self._logs.fake.uri_path(deep=random.randint(0, 6)))

    def syslog(self, infected_count=1, type=None):
        self._get_infected_list(infected_count)
        self._get_external_paths()

        # Add other types of syslogs here like DDOS, etc.
        if type == 'ransomware':
            for ip in self.infected_list:
                for ext_ip in self._logs.external_ip_list:
                    ransomware = Ransomware(src_ip=ip, external_ip=ext_ip, external_paths=self.external_paths).generate('ransomware')
                    print(ransomware.log_list)

            for ip in self.clean_list:
                ransomware = Ransomware(src_ip=ip, external_ip=None, external_paths=None).generate('clean')
                print(ransomware.log_list)


    # TODO: Add additional log types like Elastic or VPN logs
    def elastic(self, type=None):
        pass

    def splunk(self, type=None):f
        pass

    # TODO: Need to add the Windows Event classes here
    def windows_events(self, type=None):
        pass

