def test_socfaker_container_id(socfaker_fixture):
    assert socfaker_fixture.container.id

def test_socfaker_container_name(socfaker_fixture):
    assert socfaker_fixture.container.name

def test_socfaker_container_tags(socfaker_fixture):
    assert socfaker_fixture.container.tags

def test_socfaker_container_runtime(socfaker_fixture):
    assert socfaker_fixture.container.runtime