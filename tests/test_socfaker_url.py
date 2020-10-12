def test_socfaker_url_url(socfaker_fixture):
    assert socfaker_fixture.url.url

def test_socfaker_url_scheme(socfaker_fixture):
    assert socfaker_fixture.url.scheme in ['https', 'http', 'ftp', 'sftp']

def test_socfaker_url_netloc(socfaker_fixture):
    assert socfaker_fixture.url.netloc

def test_socfaker_url_path(socfaker_fixture):
    assert socfaker_fixture.url.path

def test_socfaker_url_params(socfaker_fixture):
    assert socfaker_fixture.url.params.startswith(';')

def test_socfaker_url_query(socfaker_fixture):
    assert socfaker_fixture.url.query.startswith('?')

def test_socfaker_url_port(socfaker_fixture):
    assert socfaker_fixture.url.port in ['80', '443']
