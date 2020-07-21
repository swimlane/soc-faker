def test_socfaker_registry_hive(socfaker_fixture):
    assert socfaker_fixture.registry.hive

def test_socfaker_registry_root(socfaker_fixture):
    assert socfaker_fixture.registry.root

def test_socfaker_registry_key(socfaker_fixture):
    assert socfaker_fixture.registry.key

def test_socfaker_registry_type(socfaker_fixture):
    assert socfaker_fixture.registry.type

def test_socfaker_registry_value(socfaker_fixture):
    assert socfaker_fixture.registry.value

def test_socfaker_registry_path(socfaker_fixture):
    assert socfaker_fixture.registry.path