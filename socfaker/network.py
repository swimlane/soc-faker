import random, ipaddress, requests

class Network(object):

    def __init__(self, private=False):
        self._private = private
        self.hostname = 'test'

    @property
    def ipv4(self):
        addr = ''
        if self._private:
            root = random.choice([10,172,192])
            if root == 10:
                addr = "10.%d.%d.%d" % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            elif root == 172:
                addr = "172.%d.%d.%d" % (random.randint(16, 31), random.randint(0, 255), random.randint(0, 255))
            else:
                addr = "192.168.%d.%d" % (random.randint(0,255), random.randint(0,255))
        else:
            addr = ipaddress.IPv4Address(random.getrandbits(32))
        
        return str(addr)

    @property
    def ipv6(self):
        addr = ipaddress.IPv6Address(random.getrandbits(128))

        return {
            'compressed': addr.compressed,
            'exploded': addr.exploded
        }

    def get_cidr_range(self, cidr):
        ipv4range = []
        if '/' in cidr:
            for ip in ipaddress.IPv4Network(unicode(cidr)):
                ipv4range.append(str(ip))
        return ipv4range

    @property
    def hostname(self):
        return self._hostname

    @hostname.setter
    def hostname(self, value):
        tld_list = []
        data = requests.get('https://raw.githubusercontent.com/umpirsky/tld-list/master/data/en/tld.json').json()
        for tld in data:
            tld_list.append(tld)
        wordlist = requests.get('https://raw.githubusercontent.com/elasticdog/genhost/master/wordlist')
        self._hostname = "%s.%s.%s" % (random.choice(wordlist.text.splitlines()), random.choice(wordlist.text.splitlines()),random.choice(tld_list))

    @property
    def netbios(self):
        return (self.hostname).split('.')[0]

    @property
    def mac(self):
        return "%02x:%02x:%02x:%02x:%02x:%02x" % (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )

    @property
    def protocol(self):
        return random.choice([
            'TCP',
            'UDP',
            'RPC',
            'NetBIOS',
            'SMB',
            'DHCP',
            'DNS',
            'FTP',
            'NTP',
            'IRC',
            'TELNET',
            'SSH',
            'TFTP',
            'SFTP'
        ])