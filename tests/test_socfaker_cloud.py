def test_socfaker_cloud_id(socfaker_fixture):
    assert socfaker_fixture.cloud.id

def test_socfaker_cloud_zone(socfaker_fixture):
    assert socfaker_fixture.cloud.zone

def test_socfaker_cloud_instance_id(socfaker_fixture):
    assert socfaker_fixture.cloud.instance_id

def test_socfaker_cloud_name(socfaker_fixture):
    assert socfaker_fixture.cloud.name

def test_socfaker_cloud_size(socfaker_fixture):
    assert socfaker_fixture.cloud.size

def test_socfaker_cloud_provider(socfaker_fixture):
    assert socfaker_fixture.cloud.provider

def test_socfaker_cloud_region(socfaker_fixture):
    assert socfaker_fixture.cloud.region