def test_socfaker_computer_name(socfaker_fixture):
    assert socfaker_fixture.computer.name

def test_socfaker_computer_disk(socfaker_fixture):
    assert socfaker_fixture.computer.disk

def test_socfaker_computer_memory(socfaker_fixture):
    assert socfaker_fixture.computer.memory

def test_socfaker_computer_platform(socfaker_fixture):
    assert socfaker_fixture.computer.platform

def test_socfaker_computer_mac_address(socfaker_fixture):
    assert socfaker_fixture.computer.mac_address

def test_socfaker_computer_os(socfaker_fixture):
    assert socfaker_fixture.computer.os