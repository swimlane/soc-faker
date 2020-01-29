import random, uuid

__LOCATION_LIST__ = [
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


class AzureProperties(object):

    @property
    def location(self):
        return random.choice(__LOCATION_LIST__)

    @property
    def network_zone(self):
        return random.choice(['Internal', 'InternetFacing', 'External'])
    
    @property
    def score(self):
        score_list = []
        for x in range(15):
            score_list.append(random.randint(1,10) * 10)
        return random.choice(score_list)

    @property
    def vm_name(self):
        from .computer import Computer
        return Computer().name

    @property
    def resource_group_name(self):
        from .words import Words
        word_list = []
        word_list = Words().get()
        return '{}_{}_{}'.format(random.choice(word_list), random.choice(word_list), random.choice(word_list))
        
    @property
    def resource_group_id(self):
        return str(uuid.uuid4())