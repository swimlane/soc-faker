def test_socfaker_file_name(socfaker_fixture):
    assert socfaker_fixture.file.name

def test_socfaker_file_extension(socfaker_fixture):
    assert socfaker_fixture.file.extension

def test_socfaker_file_size(socfaker_fixture):
    assert socfaker_fixture.file.size

def test_socfaker_file_timestamp(socfaker_fixture):
    assert socfaker_fixture.file.timestamp

def test_socfaker_file_accessed_timestamp(socfaker_fixture):
    assert socfaker_fixture.file.accessed_timestamp

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

def test_socfaker_file_directory(socfaker_fixture):
    assert socfaker_fixture.file.directory

def test_socfaker_file_drive_letter(socfaker_fixture):
    assert socfaker_fixture.file.drive_letter

def test_socfaker_file_gid(socfaker_fixture):
    assert socfaker_fixture.file.gid

def test_socfaker_file_type(socfaker_fixture):
    assert socfaker_fixture.file.type

def test_socfaker_file_mime_type(socfaker_fixture):
    assert socfaker_fixture.file.mime_type

def test_socfaker_file_attributes(socfaker_fixture):
    assert socfaker_fixture.file.attributes

def test_socfaker_file_version(socfaker_fixture):
    assert socfaker_fixture.file.version

def test_socfaker_file_build_version(socfaker_fixture):
    assert socfaker_fixture.file.build_version

def test_socfaker_file_checksum(socfaker_fixture):
    assert socfaker_fixture.file.checksum

def test_socfaker_file_install_scope(socfaker_fixture):
    assert socfaker_fixture.file.install_scope