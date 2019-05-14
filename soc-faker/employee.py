import random, string, pendulum

class Employee(object):

    def __init__(self):
        self.name = 'name'
        self.id = 18
        self.dob = 18

    @property
    def name(self):        
        return self._name

    @name.setter
    def name(self, value):
        firstname = random.choice(['Liam', 'Noah', 'William', 'James', 'Logan', 'Benjamin', 'Mason', 'Elijah', 'Oliver', 'Jacob', 'Emma', 'Olivia', 'Ava', 'Isabella', 'Sophia', 'Mia', 'Charlotte', 'Amelia', 'Evelyn', 'Abigail'])
        lastname = random.choice(['Smith', 'Taylor', 'Hayes', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Thompson', 'Garcia', 'Martinez', 'Johnson', 'Robinson', 'Clark', 'Rodriguez', 'Lewis', 'Lee', 'Walker', 'Hall', 'Allen', 'Young', 'Hernandez', 'Williams', 'King', 'Wright', 'Lopez', 'Hill', 'Scott', 'Green', 'Adams', 'Baker', 'Gonzalez', 'Nelson', 'Jones', 'Carter', 'Mitchell', 'Perez', 'Roberts', 'Turner', 'Phillips', 'Campbell', 'Parker', 'Evans', 'Edwards', 'Brown', 'Collins', 'Stewart', 'Sanchez', 'Morris', 'Rogers', 'Reed', 'Cook', 'Morgan', 'Bell', 'Murphy', 'Davis', 'Bailey', 'Rivera', 'Cooper', 'Richardson', 'Cox', 'Howard', 'Ward', 'Torres', 'Peterson', 'Gray', 'Miller', 'Ramirez', 'James', 'Watson', 'Brooks', 'Kelly', 'Sanders', 'Price', 'Bennett', 'Wood', 'Barnes', 'Wilson', 'Ross', 'Henderson', 'Coleman', 'Jenkins', 'Perry', 'Powell', 'Long', 'Patterson', 'Hughes', 'Flores', 'Moore', 'Washington', 'Butler', 'Simmons', 'Foster', 'Gonzales', 'Bryant', 'Alexander', 'Russell', 'Griffin', 'Diaz'])
        
        finit = firstname[:1]
        self.username = "{}{}".format(finit.lower(), lastname.lower())
        self._name = "%s %s" % (firstname, lastname)


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
        return random.choice('male', 'female', 'undisclosed')

    @property
    def ssn(self):
        # Certain numbers are invalid for United States Social Security
        # Numbers. The area (first 3 digits) cannot be 666 or 900-999.
        # The group number (middle digits) cannot be 00. The serial
        # (last 4 digits) cannot be 0000.

        area = random.randint(1, 899)
        if area == 666:
            area += 1
        group = random.randint(1, 99)
        serial = random.randint(1,9999)

        ssn = "{0:03d}-{1:02d}-{2:04d}".format(area, group, serial)
        return ssn

    @property
    def dob(self):
        return self._dob

    @dob.setter
    def dob(self, minimum_age=18):
        self._dob = pendulum.now().subtract(years=random.randint(minimum_age, 85), days=random.randint(1,365)).to_date_string()
        
    @property
    def photo(self):
        return 'https://picsum.photos/200/300?image=%s' % random.randint(0,1084)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, stringLength=18):
        lettersAndDigits = string.ascii_letters + string.digits
        randomString = ''.join(random.choice(lettersAndDigits) for i in range(stringLength))
        self._id = '00%s' % randomString

    @property
    def phone_number(self):
        first = str(random.randint(100,999))
        second = str(random.randint(1,888)).zfill(3)

        last = (str(random.randint(1,9998)).zfill(4))
        while last in ['1111','2222','3333','4444','5555','6666','7777','8888']:
            last = (str(random.randint(1,9998)).zfill(4))

        return '{}-{}-{}'.format(first,second, last)
    
    

    @property
    def language(self):
        return random.choice([
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


emp = Employee()

print(emp.name)
print(emp.name)
print(emp.language)

print(emp.id)
emp.id = 24
print(emp.id)
print(emp.dob)
print(emp.ssn)
