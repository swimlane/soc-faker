import ipaddress
from netaddr import IPNetwork
from .baseclass import BaseClass


class Network(BaseClass):

    """The Network class contains properties related to networking

    Returns:
        Network: Returns an object with properties related to network information
    """

    def __init__(self, private=False):
        super(Network, self).__init__()
        self._private = private
        self.hostname = 'test'

    @property
    def ipv4(self):
        """Returns an IPv4 IP Address

        Returns:
            str: Returns an IPv4 Address.  If private the address will be 10.x.x.x or 172.x.x.x or 192.168.x.x.
        """
        if self._private:
            root = self.random.choice([10,172,192])
            if root == 10:
                return "10.{}.{}.{}".format(self.random.randint(0, 255), self.random.randint(0, 255), self.random.randint(0, 255))
            elif root == 172:
                return "172.{}.{}.{}".format(self.random.randint(16, 31), self.random.randint(0, 255), self.random.randint(0, 255))
            else:
                return "192.168.{}.{}".format(self.random.randint(0,255), self.random.randint(0,255))
        else:
            return ipaddress.IPv4Address(self.random.getrandbits(32))

    @property
    def ipv6(self):
        """Returns an IPv6 IP Address

        Returns:
            dict: Returns a compressed and exploded IPv6 Address.
        """
        addr = ipaddress.IPv6Address(self.random.getrandbits(128))
        return {
            'compressed': addr.compressed,
            'exploded': addr.exploded
        }

    def get_cidr_range(self, cidr):
        """Returns an IPv4 range

        Returns:
            str: Returns CIDR range for an IPv4 address.
        """
        ipv4range = []
        if '/' in cidr:
            for ip in IPNetwork(cidr):
                ipv4range.append(str(ip))
        return ipv4range

    @property
    def netbios(self):
        """Returns a netbios name

        Returns:
            str: Returns a random netbios name
        """
        from .dns import DNS
        return DNS().name.split('.')[0]

    @property
    def protocol(self):
        """Random network protocol

        Returns:
            dict: Returns a random network protocol and protocol number
        """
        return self.random.choice([
            {'HOPOPT': 0},
            {'ICMP': 1},
            {'IGMP': 2},
            {'GGP': 3},
            {'IPv4': 4},
            {'ST': 5},
            {'TCP': 6},
            {'CBT': 7},
            {'EGP': 8},
            {'IGP': 9},
            {'BBN-RCC-MON': 10},
            {'NVP-II': 11},
            {'PUP': 12},
            {'EMCON': 14},
            {'XNET': 15},
            {'CHAOS': 16},
            {'UDP': 17},
            {'MUX': 18},
            {'DCN-MEAS': 19},
            {'HMP': 20},
            {'PRM': 21},
            {'XNS-IDP': 22},
            {'TRUNK-1': 23},
            {'TRUNK-2': 24},
            {'LEAF-1': 25},
            {'LEAF-2': 26},
            {'RDP': 27},
            {'IRTP': 28},
            {'ISO-TP4': 29},
            {'NETBLT': 30},
            {'MFE-NSP': 31},
            {'MERIT-INP': 32},
            {'DCCP': 33},
            {'3PC': 34},
            {'IDPR': 35},
            {'XTP': 36},
            {'DDP': 37},
            {'IDPR-CMTP': 38},
            {'TP++': 39},
            {'IL': 40},
            {'IPv6': 41},
            {'SDRP': 42},
            {'IPv6-Route': 43},
            {'IPv6-Frag': 44},
            {'IDRP': 45},
            {'RSVP': 46},
            {'GRE': 47},
            {'DSR': 48},
            {'BNA': 49},
            {'ESP': 50},
            {'AH': 51},
            {'I-NLSP': 52},
            {'NARP': 54},
            {'MOBILE': 55},
            {'TLSP': 56},
            {'SKIP': 57},
            {'IPv6-ICMP': 58},
            {'IPv6-NoNxt': 59},
            {'IPv6-Opts': 60},
            {'CFTP': 62},
            {'SAT-EXPAK': 64},
            {'KRYPTOLAN': 65},
            {'RVD': 66},
            {'IPPC': 67},
            {'SAT-MON': 69},
            {'VISA': 70},
            {'IPCV': 71},
            {'CPNX': 72},
            {'CPHB': 73},
            {'WSN': 74},
            {'PVP': 75},
            {'BR-SAT-MON': 76},
            {'SUN-ND': 77},
            {'WB-MON': 78},
            {'WB-EXPAK': 79},
            {'ISO-IP': 80},
            {'VMTP': 81},
            {'SECURE-VMTP': 82},
            {'VINES': 83},
            {'TTP': 84},
            {'IPTM': 84},
            {'NSFNET-IGP': 85},
            {'DGP': 86},
            {'TCF': 87},
            {'EIGRP': 88},
            {'OSPFIGP': 89},
            {'Sprite-RPC': 90},
            {'LARP': 91},
            {'MTP': 92},
            {'AX.25': 93},
            {'IPIP': 94},
            {'SCC-SP': 96},
            {'ETHERIP': 97},
            {'ENCAP': 98},
            {'': 99},
            {'GMTP': 100},
            {'IFMP': 101},
            {'PNNI': 102},
            {'PIM': 103},
            {'ARIS': 104},
            {'SCPS': 105},
            {'QNX': 106},
            {'A/N': 107},
            {'IPComp': 108},
            {'SNP': 109},
            {'Compaq-Peer': 110},
            {'IPX-in-IP': 111},
            {'VRRP': 112},
            {'PGM': 113},
            {'L2TP': 115},
            {'DDX': 116},
            {'IATP': 117},
            {'STP': 118},
            {'SRP': 119},
            {'UTI': 120},
            {'SMP': 121},
            {'PTP': 123},
            {'ISIS over IPv4': 124},
            {'FIRE': 125},
            {'CRTP': 126},
            {'CRUDP': 127},
            {'SSCOPMCE': 128},
            {'IPLT': 129},
            {'SPS': 130},
            {'PIPE': 131},
            {'SCTP': 132},
            {'FC': 133},
            {'RSVP-E2E-IGNORE': 134},
            {'Mobility Header': 135},
            {'UDPLite': 136},
            {'MPLS-in-IP': 137},
            {'manet': 138},
            {'HIP': 139},
            {'Shim6': 140},
            {'WESP': 141},
            {'ROHC': 142},
            {'Ethernet': 143}
        ])

    @property
    def port(self):
        """Returns a dictionary map of a port and it's common name

        Returns:
            dict: A random port and it's common name
        """
        return self.random.choice([
            {20: 'FTP'},
            {21: 'FTP'},
            {22: 'SSH'},
            {23: 'TELNET'},
            {25: 'SMTP'},
            {53: 'DNS'},
            {80: 'HTTP'},
            {110: 'POP3'},
            {119: 'NNTP'},
            {123: 'NTP'},
            {143: 'IMAP'},
            {161: 'SNMP'},
            {194: 'IRC'},
            {443: 'HTTPS'}
        ])
