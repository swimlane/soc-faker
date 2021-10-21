from pendulum import local


def test_socfaker_alert_summary(socfaker_fixture):
    assert len(str(socfaker_fixture.alert.summary).split(' ')) >= 5

def test_socfaker_alert_signature_name(socfaker_fixture):
    assert socfaker_fixture.alert.signature_name

def test_socfaker_alert_type(socfaker_fixture):
    assert socfaker_fixture.alert.type in [
        'network', 
        'host', 
        'correlation', 
        'security endpoint',
        'AwsApiCall',
        'general',
        'alert'
    ]

def test_socfaker_alert_severity_label(socfaker_fixture):
    assert socfaker_fixture.alert.severity_label in ['EMERGENCY', 'CRITICAL', 'HIGH', 'MEDIUM', 'LOW', 'INFORMATIONAL']

def test_socfaker_alert_severity_level(socfaker_fixture):
    assert isinstance(socfaker_fixture.alert.severity_level, int) and socfaker_fixture.alert.severity_level >= 0 or socfaker_fixture.alert.severity_level <= 5

def test_socfaker_alert_status(socfaker_fixture):
    assert socfaker_fixture.alert.status in ['successful', 'unsuccessful']

def test_socfaker_alert_action(socfaker_fixture):
    assert socfaker_fixture.alert.action in [
        'connection', 
        'dropped connection', 
        'initiated',
        'created',
        'completed'
    ]

def test_socfaker_alert_direction(socfaker_fixture):
    assert socfaker_fixture.alert.direction in ['from', 'to']

def test_socfaker_alert_location(socfaker_fixture):
    location = socfaker_fixture.alert.location
    if location == socfaker_fixture.alert.location:
        assert True
    assert True