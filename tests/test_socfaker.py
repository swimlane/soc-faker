def test_sockfaker_alert(socfaker_fixture):
    assert socfaker_fixture.alert

def test_socfaker_computer(socfaker_fixture):
    assert socfaker_fixture.computer

def test_socfaker_application(socfaker_fixture):
    assert socfaker_fixture.application

def test_socfaker_employee(socfaker_fixture):
    assert socfaker_fixture.employee

def test_socfaker_file(socfaker_fixture):
    assert socfaker_fixture.file

def test_socfaker_logs(socfaker_fixture):
    assert socfaker_fixture.logs

def test_socfaker_network(socfaker_fixture):
    assert socfaker_fixture.network

def test_socfaker_organization(socfaker_fixture):
    assert socfaker_fixture.organization

def test_socfaker_products(socfaker_fixture):
    assert socfaker_fixture.products

def test_socfaker_timestamp(socfaker_fixture):
    assert socfaker_fixture.timestamp

def test_socfaker_useragent(socfaker_fixture):
    assert socfaker_fixture.user_agent

def test_socfaker_vulnerability(socfaker_fixture):
    assert socfaker_fixture.vulnerability