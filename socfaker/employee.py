import string, requests
from .timestamp import Timestamp
from .baseclass import BaseClass


class Employee(BaseClass):
    """The Employee class generates random data related to an employee/user
    """

    _first_name_list = ['Liam', 'Noah', 'William', 'James', 'Logan', 'Benjamin', 'Mason', 'Elijah', 'Oliver', 'Jacob', 'Emma', 'Olivia', 'Ava', 'Isabella', 'Sophia', 'Mia', 'Charlotte', 'Amelia', 'Evelyn', 'Abigail']
    _last_name_list = ['Smith', 'Taylor', 'Hayes', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Thompson', 'Garcia', 'Martinez', 'Johnson', 'Robinson', 'Clark', 'Rodriguez', 'Lewis', 'Lee', 'Walker', 'Hall', 'Allen', 'Young', 'Hernandez', 'Williams', 'King', 'Wright', 'Lopez', 'Hill', 'Scott', 'Green', 'Adams', 'Baker', 'Gonzalez', 'Nelson', 'Jones', 'Carter', 'Mitchell', 'Perez', 'Roberts', 'Turner', 'Phillips', 'Campbell', 'Parker', 'Evans', 'Edwards', 'Brown', 'Collins', 'Stewart', 'Sanchez', 'Morris', 'Rogers', 'Reed', 'Cook', 'Morgan', 'Bell', 'Murphy', 'Davis', 'Bailey', 'Rivera', 'Cooper', 'Richardson', 'Cox', 'Howard', 'Ward', 'Torres', 'Peterson', 'Gray', 'Miller', 'Ramirez', 'James', 'Watson', 'Brooks', 'Kelly', 'Sanders', 'Price', 'Bennett', 'Wood', 'Barnes', 'Wilson', 'Ross', 'Henderson', 'Coleman', 'Jenkins', 'Perry', 'Powell', 'Long', 'Patterson', 'Hughes', 'Flores', 'Moore', 'Washington', 'Butler', 'Simmons', 'Foster', 'Gonzales', 'Bryant', 'Alexander', 'Russell', 'Griffin', 'Diaz']
    _first_name = None
    _last_name = None
    _photo_url = 'https://picsum.photos/200/300?image='

    @property
    def name(self):
        """Returns First and Last name of an employee

        Returns:
            str: Returns a random First and Last name of an employee
        """
        return "{} {}".format(self.first_name, self.last_name)

    @property
    def first_name(self):
        """First name of an employee

        Returns:
            str: Returns the first name of an employee
        """
        if not self._first_name:
            self._first_name = self.random.choice(self._first_name_list)
        return self._first_name

    @property
    def last_name(self):
        """Last name of an employee

        Returns:
            str: Returns the last name of an employee
        """
        if not self._last_name:
            self._last_name = self.random.choice(self._last_name_list)
        return self._last_name

    @property
    def username(self):
        """Username of an employee

        Returns:
            str: Returns the username of an employee
        """
        finit = self.first_name[:1]
        return "{}{}".format(finit.lower(), self.last_name.lower())

    @property
    def email(self):
        """Email of an employee

        Returns:
            str: Returns the email address of an employee
        """
        return '{}@company.com'.format(self.username)

    @property
    def gender(self):
        """Gender of an employee

        Returns:
            str: Returns the gender of an employee
        """
        return self.random.choice(['male', 'female', 'undisclosed'])

    @property
    def account_status(self):
        """Account status of an employee

        Returns:
            str: Returns an employee's account status.  This is weighted towards enabled.
        """
        return self.random.choice(['Enabled'] * 9 + ['Disabled'])

    @property
    def ssn(self):
        """SSN of an employee

        Returns:
            str: Returns the SSN of an employee
        """
        # Certain numbers are invalid for United States Social Security
        # Numbers. The area (first 3 digits) cannot be 666 or 900-999.
        # The group number (middle digits) cannot be 00. The serial
        # (last 4 digits) cannot be 0000.

        area = self.random.randint(1, 899)
        if area == 666:
            area += 1
        group = self.random.randint(1, 99)
        serial = self.random.randint(1,9999)
        return "{0:03d}-{1:02d}-{2:04d}".format(area, group, serial)

    @property
    def dob(self):
        """Date of Birth of an employee

        Returns:
            str: Returns the date of birth (DOB) of an employee
        """
        return Timestamp().date_string()

    def __get_photo_url(self):
        url = '{}{}'.format(self._photo_url, self.random.randint(0,1084))
        if requests.get(url).status_code is 200:
            return url
        else:
            self.__get_photo_url()

    @property
    def photo(self):
        """Photo URL of an employee

        Returns:
            str: Returns a URL of a random photo for the employee
        """
        return self.__get_photo_url()

    @property
    def user_id(self):
        """User ID of an employee

        Returns:
            str: Returns a random user ID of an employee
        """
        lettersAndDigits = string.ascii_letters + string.digits
        randomString = ''.join(self.random.choice(lettersAndDigits) for i in range(18))
        return '00{}'.format(randomString)

    @property
    def phone_number(self):
        """Phone number of an employee

        Returns:
            str: Returns a random phone number of an employee
        """
        first = str(self.random.randint(100,999))
        second = str(self.random.randint(1,888)).zfill(3)

        last = (str(self.random.randint(1,9998)).zfill(4))
        while last in ['1111','2222','3333','4444','5555','6666','7777','8888']:
            last = (str(self.random.randint(1,9998)).zfill(4))
        return '{}-{}-{}'.format(first,second, last)

    @property
    def logon_timestamp(self):
        """Last logon timestamp of an employee

        Returns:
            str: Returns a random ISO 8601 timestamp of an employee in the past
        """
        return Timestamp().in_the_past()

    @property
    def language(self):
        """The preferred employee language

        Returns:
            str: Returns a random language of an employee
        """
        return self.random.choice([
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
        """Employee title

        Returns:
            str: Returns a random employee title
        """
        job_title = self.random.choice([
            10 * ['Analyst'] + 5 * ['Supervisor'] + 3 * ['Manager'] + 2 * ['Director'] + 1 * ['CFO'] + 1 * ['CISO'] + 1 * ['CIO'] + 1 * ['CEO']
        ])
        if job_title not in ['CFO', 'CISO', 'CIO', 'CEO']:
            return "{}, {}".format(self.random.choice(self.department), job_title)
        return job_title

    @property
    def department(self):
        """Employee department

        Returns:
            str: Returns a random employee department
        """
        return self.random.choice([
            10 * ['SOC'] + 10 * ['NOC'] + 5 * ['Help Desk'] + 5 * ['HR'] + 4 * ['QA']
        ])
