import random

class Application(object):

    def __init__(self):

    self.logon_timestamp = 120
    
    @property 
    def status(self):
        return random.choice('Active', 'Inactive', 'Legacy')

    @property
    def name(self):
        return random.choice([
            'DropBox',
            'Office 365',
            'GSuite',
            'Rindle',
            'JIRA',
            'ZenDesk',
            'Jenkins',
            'GitHub',
            'GitLab',
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

    @setter.logon_timestamp
    def logon_timestamp(self, value):
        if isinstance(value, int):
            self._logon_timestamp = pendulum.now().subtract(days=random.randint(1,value), hours=random.randint(1,59), minutes=random.randint(1,59), seconds=random.randint(1,59))