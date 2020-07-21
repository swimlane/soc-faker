def test_socfaker_operating_system_family(socfaker_fixture):
    assert socfaker_fixture.operating_system.family

def test_socfaker_operating_system_name(socfaker_fixture):
    assert socfaker_fixture.operating_system.name

def test_socfaker_operating_system_version(socfaker_fixture):
    assert socfaker_fixture.operating_system.version

def test_socfaker_operating_system_fullname(socfaker_fixture):
    assert socfaker_fixture.operating_system.fullname