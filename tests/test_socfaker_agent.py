def test_socfaker_agent_ephermal_id(socfaker_fixture):
    assert len(socfaker_fixture.agent.ephermeral_id) == 8

def test_socfaker_agent_ephermal_id_not_duplicate(socfaker_fixture):
    assert socfaker_fixture.agent.ephermeral_id != socfaker_fixture.agent.ephermeral_id

def test_socfaker_agent_id(socfaker_fixture):
    assert len(socfaker_fixture.agent.id) == 8

def test_socfaker_agent_id_not_duplicate(socfaker_fixture):
    assert socfaker_fixture.agent.id != socfaker_fixture.agent.id

def test_socfaker_agent_name(socfaker_fixture):
    assert str(socfaker_fixture.agent.name).split('-')[0] in ['Desktop', 'Laptop']

def test_socfaker_agent_type(socfaker_fixture):
    assert socfaker_fixture.agent.type in ['filebeat', 'auditbeat', 'functionbeat', 'heartbeat', 'winlogbeat', 'packetbeat']

def test_socfaker_agent_version(socfaker_fixture):
    assert socfaker_fixture.agent.version == '7.8.0'