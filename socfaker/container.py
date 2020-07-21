from .network import Network
from .words import Words
from .baseclass import BaseClass


class Container(BaseClass):

    """The Container class contains general properties related to containers

    Returns:
        Container: An object containing properties related to containers
    """
    _words = Words().get()

    @property
    def id(self):
        """A container ID

        Returns:
            str: A hex container ID
        """
        return str(self.uuid.uuid4().hex)

    @property
    def name(self):
        """A random generated container name

        Returns:
            str: A randomly generated container name
        """
        try:
            return ''.join(self.random.choices(self._words, k=self.random.randint(1,3)))
        except:
            return ''.join(self.random.sample(self._words, self.random.randint(1,3)))
    @property
    def tags(self):
        """Container tags

        Returns:
            list: A random list of container tags
        """
        return_list = []
        for count in range(self.random.randint(1,5)):
            return_list.append(self.random.choice(self._words))
        return return_list

    @property
    def runtime(self):
        """A container runtime

        Returns:
            str: Returns either docker or kubernetes
        """
        return self.random.choice(['docker', 'kubernetes'])
