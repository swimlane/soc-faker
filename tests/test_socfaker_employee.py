def test_socfaker_employee_name(socfaker_fixture):
    assert socfaker_fixture.employee.name

def test_socfaker_employee_first_name(socfaker_fixture):
    assert socfaker_fixture.employee.first_name

def test_socfaker_employee_last_name(socfaker_fixture):
    assert socfaker_fixture.employee.last_name

def test_socfaker_employee_username(socfaker_fixture):
    assert socfaker_fixture.employee.username

def test_socfaker_employee_email(socfaker_fixture):
    assert socfaker_fixture.employee.email

def test_socfaker_employee_gender(socfaker_fixture):
    assert socfaker_fixture.employee.gender

def test_socfaker_employee_account_status(socfaker_fixture):
    assert socfaker_fixture.employee.account_status

def test_socfaker_employee_ssn(socfaker_fixture):
    assert socfaker_fixture.employee.ssn

def test_socfaker_employee_dob(socfaker_fixture):
    assert socfaker_fixture.employee.dob

def test_socfaker_employee_photo(socfaker_fixture):
    assert socfaker_fixture.employee.photo

def test_socfaker_employee_user_id(socfaker_fixture):
    assert socfaker_fixture.employee.user_id

def test_socfaker_employee_phone_number(socfaker_fixture):
    assert socfaker_fixture.employee.phone_number

def test_socfaker_employee_logon_timestamp(socfaker_fixture):
    assert socfaker_fixture.employee.logon_timestamp

def test_socfaker_employee_language(socfaker_fixture):
    assert socfaker_fixture.employee.language

def test_socfaker_employee_title(socfaker_fixture):
    assert socfaker_fixture.employee.title

def test_socfaker_employee_department(socfaker_fixture):
    assert socfaker_fixture.employee.department