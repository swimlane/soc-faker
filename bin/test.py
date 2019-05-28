import random
from socfaker import Application, Computer, Employee, File, Network, Organization, Vulnerability, VulnerabilityHost, VulnerabilityScan

vuln_host = VulnerabilityHost(
            critical=random.randint(1,3),
            high=random.randint(1,3),
            medium=random.randint(1,3),
            low=random.randint(1,3),
            informational=random.randint(1,3)
        )

print(vuln_host.name)