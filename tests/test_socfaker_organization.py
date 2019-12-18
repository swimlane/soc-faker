def test_socfaker_organization_name(socfaker_fixture):
    assert socfaker_fixture.organization.name

def test_socfaker_organization_division(socfaker_fixture):
    assert socfaker_fixture.organization.division

def test_socfaker_organization_title(socfaker_fixture):
    assert socfaker_fixture.organization.title
