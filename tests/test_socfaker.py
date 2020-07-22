def test_sockfaker_agent(socfaker_fixture):
    assert socfaker_fixture.agent

def test_sockfaker_alert(socfaker_fixture):
    assert socfaker_fixture.alert

def test_sockfaker_application(socfaker_fixture):
    assert socfaker_fixture.application

def test_sockfaker_cloud(socfaker_fixture):
    assert socfaker_fixture.cloud

def test_socfaker_computer(socfaker_fixture):
    assert socfaker_fixture.computer

def test_sockfaker_container(socfaker_fixture):
    assert socfaker_fixture.container

def test_sockfaker_dns(socfaker_fixture):
    assert socfaker_fixture.dns

def test_socfaker_employee(socfaker_fixture):
    assert socfaker_fixture.employee

def test_socfaker_file(socfaker_fixture):
    assert socfaker_fixture.file

def test_sockfaker_http(socfaker_fixture):
    assert socfaker_fixture.http

def test_sockfaker_location(socfaker_fixture):
    assert socfaker_fixture.location

def test_socfaker_logs(socfaker_fixture):
    assert socfaker_fixture.logs

def test_socfaker_network(socfaker_fixture):
    assert socfaker_fixture.network

def test_sockfaker_operating_system(socfaker_fixture):
    assert socfaker_fixture.operating_system

def test_socfaker_organization(socfaker_fixture):
    assert socfaker_fixture.organization

def test_sockfaker_process(socfaker_fixture):
    assert socfaker_fixture.process

def test_socfaker_products(socfaker_fixture):
    assert socfaker_fixture.products

def test_sockfaker_registry(socfaker_fixture):
    assert socfaker_fixture.registry

def test_socfaker_timestamp(socfaker_fixture):
    assert socfaker_fixture.timestamp

def test_socfaker_useragent(socfaker_fixture):
    assert socfaker_fixture.user_agent

def test_socfaker_vulnerability(socfaker_fixture):
    assert socfaker_fixture.vulnerability()

def test_sockfaker_words(socfaker_fixture):
    assert socfaker_fixture.words