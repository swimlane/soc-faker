import random
from .computer import Computer
from .baseclass import BaseClass


class Agent(BaseClass):

    """Agent class is used to simulate or fake data related to logging agent,
    similar to Elastic's Winlogbeat

    Attributes:
        ephermal_id (str): A unique 8 character length hex ID.
        id (str): A unique 8 character legnth ID representing the agent ID
        name (str): The agent name
        type (str): The agent type, in this case the name of the beat
        version (str): Current beat version which is 7.8.0

    Returns:
        Agent: A Elastic beats agent
    """

    _agent_id = None

    @property
    def ephermeral_id(self):
        """A unique and random ephermal ID that changes

        Returns:
            str: A unique 8 character length hex ID
        """
        return ''.join([self.random.choice('0123456789ABCDEF') for x in range(8)])

    @property
    def id(self):
        """A agent ID which is typically static across the lifetime of the 
           agent (per instance of this class)

        Returns:
            str: A static but unique 8 character length ID representing the agent ID
        """
        if not self._agent_id:
            self._agent_id = ''.join([self.random.choice('0123456789ABCDEF') for x in range(8)])
        return self._agent_id

    @property
    def name(self):
        """A custom name of the agent

        Returns:
            str: A custom name of the agent
        """
        return Computer().name

    @property
    def type(self):
        """The type of agent.

        Options are: 'filebeat', 'auditbeat', 'functionbeat', 
                     'heartbeat', 'winlogbeat', 'packetbeat'

        Returns:
            str: A agent type
        """
        return self.random.choice([
            'filebeat', 
            'auditbeat', 
            'functionbeat', 
            'heartbeat', 
            'winlogbeat', 
            'packetbeat'
        ])

    @property
    def version(self):
        """The agent version

        Returns:
            str: Currently set to a static value of 7.8.0
        """
        return '7.8.0'
