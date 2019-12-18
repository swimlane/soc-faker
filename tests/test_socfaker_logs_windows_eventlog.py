def test_socfaker_logs_windows_eventlog(socfaker_fixture):
    assert socfaker_fixture.logs.windows.eventlog()

def test_socfaker_logs_windows_sysmon_logs(socfaker_fixture):
    assert socfaker_fixture.logs.windows.sysmon()