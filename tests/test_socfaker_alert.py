def test_socfaker_alert_summary(socfaker_fixture):
    assert socfaker_fixture.alert.summary

def test_socfaker_alert_signature_name(socfaker_fixture):
    assert socfaker_fixture.alert.signature_name

def test_socfaker_alert_type(socfaker_fixture):
    assert socfaker_fixture.alert.type

def test_socfaker_alert_status(socfaker_fixture):
    assert socfaker_fixture.alert.status

def test_socfaker_alert_action(socfaker_fixture):
    assert socfaker_fixture.alert.action

def test_socfaker_alert_direction(socfaker_fixture):
    assert socfaker_fixture.alert.direction

def test_socfaker_alert_location(socfaker_fixture):
    assert socfaker_fixture.alert.location