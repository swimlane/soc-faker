import random, string, pendulum, requests


class Employee(object):

    def __init__(self):
        self.name = ''
        self.logon_timestamp = 120
        self.user_id = 18
        self.dob = 18
        self.gender = ''
        self.language = ''
        self.account_status = ''
        self.ssn = ''
        self.photo = ''
        self.phone_number = ''
        self.department = ''

    @property
    def name(self):        
        return self._name

    @name.setter
    def name(self, value):
        firstname = random.choice(['Liam', 'Noah', 'William', 'James', 'Logan', 'Benjamin', 'Mason', 'Elijah', 'Oliver', 'Jacob', 'Emma', 'Olivia', 'Ava', 'Isabella', 'Sophia', 'Mia', 'Charlotte', 'Amelia', 'Evelyn', 'Abigail'])
        lastname = random.choice(['Smith', 'Taylor', 'Hayes', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Thompson', 'Garcia', 'Martinez', 'Johnson', 'Robinson', 'Clark', 'Rodriguez', 'Lewis', 'Lee', 'Walker', 'Hall', 'Allen', 'Young', 'Hernandez', 'Williams', 'King', 'Wright', 'Lopez', 'Hill', 'Scott', 'Green', 'Adams', 'Baker', 'Gonzalez', 'Nelson', 'Jones', 'Carter', 'Mitchell', 'Perez', 'Roberts', 'Turner', 'Phillips', 'Campbell', 'Parker', 'Evans', 'Edwards', 'Brown', 'Collins', 'Stewart', 'Sanchez', 'Morris', 'Rogers', 'Reed', 'Cook', 'Morgan', 'Bell', 'Murphy', 'Davis', 'Bailey', 'Rivera', 'Cooper', 'Richardson', 'Cox', 'Howard', 'Ward', 'Torres', 'Peterson', 'Gray', 'Miller', 'Ramirez', 'James', 'Watson', 'Brooks', 'Kelly', 'Sanders', 'Price', 'Bennett', 'Wood', 'Barnes', 'Wilson', 'Ross', 'Henderson', 'Coleman', 'Jenkins', 'Perry', 'Powell', 'Long', 'Patterson', 'Hughes', 'Flores', 'Moore', 'Washington', 'Butler', 'Simmons', 'Foster', 'Gonzales', 'Bryant', 'Alexander', 'Russell', 'Griffin', 'Diaz'])
        
        self._firstName = firstname
        self._lastName = lastname

        finit = firstname[:1]
        self.username = "{}{}".format(finit.lower(), lastname.lower())
        self._name = "%s %s" % (firstname, lastname)

    @property
    def first_name(self):
        return self._firstName

    @property
    def last_name(self):
        return self._lastName

    @property
    def username(self):
        return self._username
        
    @username.setter
    def username(self, value):
        self.email = value
        self._username = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = '%s@company.com' % value

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = random.choice(['male', 'female', 'undisclosed'])

    @property
    def account_status(self):
        return self._accountStatus
        
    @account_status.setter
    def account_status(self, value):
        self._accountStatus = random.choice(['Enabled'] * 9 + ['Disabled'])

    @property
    def ssn(self):
        return self._ssn

    @ssn.setter
    def ssn(self, value):
        # Certain numbers are invalid for United States Social Security
        # Numbers. The area (first 3 digits) cannot be 666 or 900-999.
        # The group number (middle digits) cannot be 00. The serial
        # (last 4 digits) cannot be 0000.

        area = random.randint(1, 899)
        if area == 666:
            area += 1
        group = random.randint(1, 99)
        serial = random.randint(1,9999)

        self._ssn = "{0:03d}-{1:02d}-{2:04d}".format(area, group, serial)

    @property
    def dob(self):
        return self._dob

    @dob.setter
    def dob(self, minimum_age=18):
        self._dob = pendulum.now().subtract(years=random.randint(minimum_age, 85), days=random.randint(1,365)).to_date_string()
        
    @property
    def photo(self):
        return self._photo

    @photo.setter
    def photo(self, value):
        url = 'https://picsum.photos/200/300?image=%s' % random.randint(0,1084)
        if requests.get(url).status_code is 200:
            self._photo = url
        else:
            self.photo = ''

    @property
    def user_id(self):
        return self._userId

    @user_id.setter
    def user_id(self, stringLength=18):
        lettersAndDigits = string.ascii_letters + string.digits
        randomString = ''.join(random.choice(lettersAndDigits) for i in range(stringLength))
        self._userId = '00%s' % randomString

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        first = str(random.randint(100,999))
        second = str(random.randint(1,888)).zfill(3)

        last = (str(random.randint(1,9998)).zfill(4))
        while last in ['1111','2222','3333','4444','5555','6666','7777','8888']:
            last = (str(random.randint(1,9998)).zfill(4))

        self._phone_number = '{}-{}-{}'.format(first,second, last)
    
    @property
    def logon_timestamp(self):
        return self._logon_timestamp

    @logon_timestamp.setter
    def logon_timestamp(self, value):
        if isinstance(value, int):
            self._logon_timestamp = pendulum.now().subtract(days=random.randint(1,value), hours=random.randint(1,59), minutes=random.randint(1,59), seconds=random.randint(1,59))

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        self._language = random.choice([
            "bn-BD",
            "bn-IN",
            "zh-CN",
            "zh-TW",
            "zh-HK",
            "nl-BE",
            "nl-NL",
            "en-GB",
            "en-US",
            "en-CA",
            "en-IN",
            "en-AU",
            "en-NZ",
            "fr-BE",
            "fr-CH",
            "fr-FR",
            "fr-CA",
            "de-AT",
            "de-DE",
            "de-CH",
            "it-CH",
            "it-IT",
            "pt-PT",
            "pt-BR",
            "es-ES",
            "es-MX",
            "es-AR",
            "es-CO",
            "es-CL",
            "es-US",
            "ta-IN",
            "ta-LK"
        ])

    @property
    def title(self):
        job_titles = \
            10 * ['Analyst'] + \
            5 * ['Supervisor'] + \
            3 * ['Manager'] + \
            2 * ['Director'] + \
            1 * ['CFO'] + \
            1 * ['CISO'] + \
            1 * ['CIO'] + \
            1 * ['CEO']

        job_title = random.choice(job_titles)

        if job_title not in ['CFO', 'CISO', 'CIO', 'CEO']:
            return "{}, {}".format(random.choice(self.department), job_title)
        return job_title

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, value):
        departments = \
            10 * ['SOC'] + \
            10 * ['NOC'] + \
            5 * ['Help Desk'] + \
            5 * ['HR'] + \
            4 * ['QA']
        self._department = random.choice(departments)