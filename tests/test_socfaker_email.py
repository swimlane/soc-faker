
def test_socfaker_email_received_from(socfaker_fixture):
    assert socfaker_fixture.email.received_from

def test_socfaker_email_x_headers(socfaker_fixture):
    assert socfaker_fixture.email.x_headers

def test_socfaker_email_date(socfaker_fixture):
    assert socfaker_fixture.email.date

def test_socfaker_email_to_address(socfaker_fixture):
    assert socfaker_fixture.email.to_address
    assert '@' in socfaker_fixture.email.to_address 

def test_socfaker_email_from_address(socfaker_fixture):
    assert socfaker_fixture.email.from_address
    assert '@' in socfaker_fixture.email.from_address

def test_socfaker_email_subject(socfaker_fixture):
    assert socfaker_fixture.email.subject

def test_socfaker_email_message_id(socfaker_fixture):
    assert socfaker_fixture.email.message_id

def test_socfaker_email_x_mailer(socfaker_fixture):
    assert socfaker_fixture.email.x_mailer

def test_socfaker_email_in_reply_to(socfaker_fixture):
    assert socfaker_fixture.email.in_reply_to

def test_socfaker_email_body(socfaker_fixture):
    assert socfaker_fixture.email.body

def test_socfaker_email_email(socfaker_fixture):
    assert socfaker_fixture.email.email