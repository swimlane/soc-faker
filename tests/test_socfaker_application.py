def test_socfaker_application_status(socfaker_fixture):
    assert socfaker_fixture.application.status in ['Active', 'Inactive', 'Legacy']

def test_socfaker_application_account_status(socfaker_fixture):
    assert socfaker_fixture.application.account_status in ['Enabled', 'Disabled']

def test_socfaker_name(socfaker_fixture):
    assert socfaker_fixture.application.name

def test_socfaker_application_logon_timestamp(socfaker_fixture):
    assert socfaker_fixture.application.logon_timestamp