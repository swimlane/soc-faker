def test_socfaker_logs_syslog(socfaker_fixture):
    assert socfaker_fixture.logs.syslog(count=1)

def test_socfaker_logs_windows(socfaker_fixture):
    assert socfaker_fixture.logs.windows