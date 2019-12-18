import random, pendulum


class Application(object):

    def __init__(self):
        self.logon_timestamp = 45
        self.status = ''
        self.account_status = ''
        self.name = ''

    @property 
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = random.choice(['Active', 'Inactive', 'Legacy'])

    @property
    def account_status(self):
        return self._accountStatus

    @account_status.setter
    def account_status(self, value):
        self._accountStatus = random.choice(['Enabled'] * 9 + ['Disabled'])

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = random.choice([
            'DropBox',
            'Office 365',
            'GSuite',
            'JIRA',
            'ZenDesk',
            'GitHub',
            'Swimlane',
            'Microsoft Azure',
            'Amazon Web Services',
            'Carbon Black',
            'Salesforce',
            'ServiceNow',
            'Slack',
            'Splunk',
            'Zoom',
            'ZScaler'
        ])

    @property
    def logon_timestamp(self):
        return self._logon_timestamp

    @logon_timestamp.setter
    def logon_timestamp(self, value):
        if isinstance(value, int):
            self._logon_timestamp = pendulum.now().subtract(days=random.randint(1,value), hours=random.randint(1,59), minutes=random.randint(1,59), seconds=random.randint(1,59))