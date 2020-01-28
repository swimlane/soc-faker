def test_socfaker_registry_hive(socfaker_fixture):
    assert socfaker_fixture.registry.hive

def test_socfaker_registry_path(socfaker_fixture):
    assert socfaker_fixture.registry.path