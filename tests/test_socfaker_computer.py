def test_socfaker_computer_name(socfaker_fixture):
    assert socfaker_fixture.computer.name
    assert str(socfaker_fixture.computer.name).split('-')[0] in ['Desktop', 'Laptop']

def test_socfaker_computer_disk(socfaker_fixture):
    assert socfaker_fixture.computer.disk
    assert len(socfaker_fixture.computer.disk) == 5

def test_socfaker_computer_memory(socfaker_fixture):
    assert socfaker_fixture.computer.memory
    assert len(socfaker_fixture.computer.memory) == 5

def test_socfaker_computer_platform(socfaker_fixture):
    assert socfaker_fixture.computer.platform

def test_socfaker_computer_mac_address(socfaker_fixture):
    assert socfaker_fixture.computer.mac_address
    assert len(socfaker_fixture.computer.mac_address.split(':')) == 6

def test_socfaker_computer_os(socfaker_fixture):
    assert socfaker_fixture.computer.os

def test_socfaker_computer_ipv4(socfaker_fixture):
    assert socfaker_fixture.computer.ipv4
