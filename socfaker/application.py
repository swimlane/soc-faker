from .timestamp import Timestamp
from .baseclass import BaseClass


class Application(BaseClass):

    """Application object contains properties for a random 
       (non-specific) application
    """

    @property 
    def status(self):
        """Returns the application status

        Returns:
            str: Returns the application status of 
                 Active, Inactive, or Legacy
        """
        return self.random.choice(['Active', 'Inactive', 'Legacy'])

    @property
    def account_status(self):
        """A random account status for the application

        Returns:
            str: Returns whether an account is enabled or 
                 disabled for an application
        """
        return self.random.choice(['Enabled'] * 9 + ['Disabled'])

    @property
    def name(self):
        """The name of an application

        Returns:
            str: Returns a random application name based on common 
                 applications used in enterprises
        """
        return self.random.choice([
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
        """Logon timestamp of a user/service for an applicaiton

        Returns:
            str: Returns an ISO 8601 timestamp in the past
        """
        return Timestamp().in_the_past()
