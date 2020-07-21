def test_socfaker_network_ipv4(socfaker_fixture):
    assert socfaker_fixture.network.ipv4

def test_socfaker_network_ipv6(socfaker_fixture):
    assert socfaker_fixture.network.ipv6

def test_socfaker_network_ipv4range(socfaker_fixture):
    assert '192.168.1.32' in socfaker_fixture.network.get_cidr_range('192.168.1.0/24') 

def test_socfaker_network_netbios(socfaker_fixture):
    assert socfaker_fixture.network.netbios

def test_socfaker_network_protocol(socfaker_fixture):
    assert socfaker_fixture.network.protocol

def test_socfaker_network_port(socfaker_fixture):
    assert socfaker_fixture.network.port