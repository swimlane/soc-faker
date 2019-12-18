def test_socfaker_azure(socfaker_fixture):
    assert socfaker_fixture.products.azure

def test_socfaker_elastic(socfaker_fixture):
    assert socfaker_fixture.products.elastic
    
def test_socfaker_qualysguard(socfaker_fixture):
    assert socfaker_fixture.products.qualysguard

def test_socfaker_servicenow(socfaker_fixture):
    assert socfaker_fixture.products.servicenow