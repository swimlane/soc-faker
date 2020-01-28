def test_socfaker_file_filename(socfaker_fixture):
    print(socfaker_fixture.file.filename)
    assert socfaker_fixture.file.filename

def test_socfaker_file_size(socfaker_fixture):
    assert socfaker_fixture.file.size

def test_socfaker_file_timestamp(socfaker_fixture):
    assert socfaker_fixture.file.timestamp

def test_socfaker_file_hashes(socfaker_fixture):
    assert socfaker_fixture.file.hashes

def test_socfaker_file_md5(socfaker_fixture):
    assert socfaker_fixture.file.md5

def test_socfaker_file_sha1(socfaker_fixture):
    assert socfaker_fixture.file.sha1

def test_socfaker_file_sha256(socfaker_fixture):
    assert socfaker_fixture.file.sha256

def test_socfaker_file_full_path(socfaker_fixture):
    assert socfaker_fixture.file.full_path

def test_socfaker_file_signed(socfaker_fixture):
    assert socfaker_fixture.file.signed
           
def test_socfaker_file_signature(socfaker_fixture):
    assert socfaker_fixture.file.signature

def test_socfaker_file_signature_status(socfaker_fixture):
    assert socfaker_fixture.file.signature_status

    