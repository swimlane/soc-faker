from .baseclass import BaseClass


class AzureProperties(BaseClass):

    """Class containing common properties for Microsoft Azure

    Returns:
        AzureProperties: A object containing common properties for Microsoft Azure
    """

    __LOCATION_LIST = [
                        'eastasia',
                        'southeastasia',
                        'centralus',
                        'eastus',
                        'eastus2',
                        'westus',
                        'northcentralus',
                        'southcentralus',
                        'northeurope',
                        'westeurope',
                        'japanwest',
                        'japaneast',
                        'brazilsouth',
                        'australiaeast',
                        'australiasoutheast',
                        'southindia',
                        'centralindia',
                        'westindia',
                        'canadacentral',
                        'canadaeast',
                        'uksouth',
                        'ukwest',
                        'westcentralus',
                        'westus2',
                        'koreacentral',
                        'koreasouth',
                        'francecentral',
                        'francesouth',
                        'australiacentral',
                        'australiacentral2',
                        'southafricanorth',
                        'southafricawest'
                        ]

    @property
    def location(self):
        """A location based on Microsoft Azure available locations

        Returns:
            str: Returns a Azure location
        """
        return self.random.choice(self.__LOCATION_LIST)

    @property
    def network_zone(self):
        """Network zone type in Microsoft Azure

        Returns:
            str: Returns a random type for a network zone in Azure
        """
        return self.random.choice(['Internal', 'InternetFacing', 'External'])
    
    @property
    def score(self):
        score_list = []
        for x in range(15):
            score_list.append(self.random.randint(1,10) * 10)
        return self.random.choice(score_list)

    @property
    def vm_name(self):
        """A Azure VM Name

        Returns:
            str: Returns a random Azure VM name
        """
        from .computer import Computer
        return Computer().name

    @property
    def resource_group_name(self):
        """Resource Group Name in Azure

        Returns:
            str: Returns a three-word Resource Group name for Microsoft Azure
        """
        from .words import Words
        word_list = []
        word_list = Words().get()
        return '{}_{}_{}'.format(
            self.random.choice(word_list), 
            self.random.choice(word_list), 
            self.random.choice(word_list)
        )

    @property
    def resource_group_id(self):
        """Resource Group ID

        Returns:
            str: Returns a random resource group ID (GUID)
        """
        return str(self.uuid.uuid4())
