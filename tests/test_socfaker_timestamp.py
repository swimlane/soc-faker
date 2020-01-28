def test_socfaker_timestamp_in_the_past(socfaker_fixture):
    assert socfaker_fixture.timestamp.in_the_past()

def test_socfaker_timestamp_in_the_future(socfaker_fixture):
    assert socfaker_fixture.timestamp.in_the_future()

def test_socfaker_timestamp_current(socfaker_fixture):
    assert socfaker_fixture.timestamp.current