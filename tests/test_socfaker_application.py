def test_socfaker_application_status(socfaker_fixture):
    assert socfaker_fixture.application.status

def test_socfaker_application_account_status(socfaker_fixture):
    assert socfaker_fixture.application.account_status

def test_socfaker_name(socfaker_fixture):
    assert socfaker_fixture.application.name

def test_socfaker_application_logon_timestamp(socfaker_fixture):
    assert socfaker_fixture.application.logon_timestamp