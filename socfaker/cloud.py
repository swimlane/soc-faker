import string
from .network import Network
from .computer import Computer
from .baseclass import BaseClass


class Cloud(BaseClass):

    """The Cloud class contains properties related to cloud resources.  The initial properties of this object are based on Elastics ECS properties.

    Returns:
        Cloud: Returns a Cloud object containing common cloud properties
    """
    _agent_id = None

    @property
    def id(self):
        """A cloud instance ID

        Returns:
            str: A random GUID for a cloud instance ID
        """
        return str(self.uuid.uuid4())

    @property
    def zone(self):
        """A random generated availability zone in common cloud platforms like AWS & Azure

        Returns:
            str: A string representing a cloud availability zone
        """
        return '{}-{}-{}'.format(
            self.random.choice([
                'us', 
                'af', 
                'ap', 
                'ca', 
                'eu', 
                'me', 
                'sa'
            ]),
            self.random.choice([
                'east', 
                'west', 
                'south', 
                'north', 
                'northeast', 
                'southeast', 
                'northwest', 
                'central'
            ]),
            self.random.randint(1,5)
        )

    @property
    def instance_id(self):
        """A random hex instance ID

        Returns:
            str: A random HEX character instance ID
        """
        return 'i-{}'.format(''.join([self.random.choice('0123456789ABCDEF') for x in range(17)]))

    @property
    def name(self):
        """The name of a cloud VM/container instance

        Returns:
            str: A random generated name of a cloud VM or container instance
        """
        prefix = self.random.choice([
            'docker', 
            'k8', 
            'cluster', 
            'prod', 
            'qa', 
            'dev', 
            'client', 
            'server'
        ])
        return '{}-{}'.format(
            prefix, 
            ''.join(
                self.random.choice(
                    string.ascii_uppercase + string.digits) for _ in range(7)))

    @property
    def size(self):
        """The size of a instance (based on AWS naming convention)

        Returns:
            str: A random size of an instance based on AWS naming convention
        """
        return '{}.{}'.format(
            self.random.choice([
                't1', 
                't2', 
                'a1', 
                'm5', 
                'm4'
            ]),
            self.random.choice([
                'medium', 
                'micro', 
                'large', 
                'xlarge', 
                '2xlarge', 
                '4xlarge', 
                'metal'
            ])
        )

    @property
    def provider(self):
        """The cloud provider

        Returns:
            str: A random cloud provider of either aws, azure, gcp, or digitalocean
        """
        return self.random.choice([
            'aws', 
            'azure', 
            'gcp', 
            'digitalocean'
        ])

    @property
    def region(self):
        """The region of a cloud instance

        Returns:
            str: The region of a cloud instance
        """
        return self.zone
