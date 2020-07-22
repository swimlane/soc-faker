def test_socfaker_agent_ephermal_id(socfaker_fixture):
    assert socfaker_fixture.agent.ephermeral_id

def test_socfaker_agent_id(socfaker_fixture):
    assert socfaker_fixture.agent.id

def test_socfaker_agent_name(socfaker_fixture):
    assert socfaker_fixture.agent.name

def test_socfaker_agent_type(socfaker_fixture):
    assert socfaker_fixture.agent.type

def test_socfaker_agent_version(socfaker_fixture):
    assert socfaker_fixture.agent.version