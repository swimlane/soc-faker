import random, requests, json, ipaddress, string

class Computer(object):

    def __init__(self):
        self.name = 'test'
        self.os = 'os'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        prefix = random.choice(['Desktop'] * 4 + ['Laptop'])
        self._name = '%s-' % prefix + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))

    @property
    def disk(self):
        disk_size_list = []
        precision = 2
        size = random.randint(1, 1099511627776)
        suffixes=['B','KB','MB','GB','TB']
        suffixIndex = 0
        while size > 1024 and suffixIndex < 4:
            suffixIndex += 1 #increment the index of the suffix
            size = size/1024.0 #apply the division
            disk_size_list.append("%.*f%s"%(precision,size,suffixes[suffixIndex]))
        
        return disk_size_list

    @property
    def memory(self):
        mem_size_list = []
        precision = 2
        gig_size = random.randint(1,32)
        size = gig_size * 1073741824

        suffixes=['B','KB','MB','GB','TB']
        suffixIndex = 0
        while size > 1024 and suffixIndex < 4:
            suffixIndex += 1 #increment the index of the suffix
            size = size/1024.0 #apply the division
            mem_size_list.append("%.*f%s"%(precision,size,suffixes[suffixIndex]))
        
        return mem_size_list

    @property
    def platform(self):
        return random.choice(['Laptop', 'Desktop', 'Workstation', 'Server', 'Virtual Machine', 'Container', 'Micro-Service', 'Droplet', 'SaaS'])

    @property
    def mac_address(self):
        return ':'.join("%02x"%random.randint(0, 255) for _ in range(5))
        
    @property
    def os(self):
        return self._os

    @os.setter
    def os(self, value):
        self._os = random.choice([
            'Apple III',
            'Red Hat Linux',
            'CentOS',
            'Fedora',
            'openSUSE',
            'Oracle Linux',
            'SUSE Linux',
            'Ubunutu GNOME',
            'Apple Lisa',
            'Apple Macintosh',
            'Classic Mac OS',
            'Rhapsody',
            'macOS',
            'macOS Server',
            'iOS',
            'watchOS',
            'tvOS',
            'DOS',
            'Android 4.0.1', 
            'Chrome OS',
            'Windows 3.1x',
            'Windows 95',
            'Windows 98',
            'Windows Millennium Edition',
            'Windows NT',
            'Windows NT 3.1',
            'Windows NT 3.5',
            'Windows NT 3.51',
            'Windows NT 4.0',
            'Windows 2000',
            'Windows XP',
            'Windows Server 2003',
            'Windows Vista',
            'Windows Home Server', 
            'Windows Server 2008',
            'Windows 7',
            'Windows Server 2008 R2',
            'Windows Server 2012',
            'Windows 8',
            'Windows 8.1',
            'Windows Server 2012 R2',
            'Windows 10',
            'Windows Server 2016',
            'Windows Server 2019',
            'Windows CE',
            'Novell',
            'UnixWare',
            'BSD',
            'FreeBSD',
            'OpenBSD',
            'Darwin',
            'GNU'])
