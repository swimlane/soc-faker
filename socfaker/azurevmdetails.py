from .computer import Computer
from .words import Words
from .baseclass import BaseClass


class AzureVMDetails(BaseClass):
      
    """An object containing Microsoft Azure VM Details (properties)
    """
    __SIZE_LIST = [
      'Standard_B1ls1',
      'Standard_B1s',
      'Standard_B1ms',
      'Standard_B2s',
      'Standard_B2ms',
      'Standard_B8ms',
      'Standard_B4ms',
      'Standard_B12ms',
      'Standard_B16ms',
      'Standard_B20ms'
    ]

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

    def __init__(self):
        super(AzureVMDetails, self).__init__()
        self.word_list = Words().get()

    def __get_unique_ids(self):
        return_dict = {}
        return_dict['subscription_id'] = str(self.uuid.uuid4())
        return_dict['vm_id'] = str(self.uuid.uuid4())
        return return_dict

    def __os_type(self):
        return_dict = {}
        os_type = self.random.choice(['Windows', 'RedHat', 'CentOS'])
        if os_type == 'Windows':
            return_dict = {
                'os': os_type,
                'publisher': self.random.choice(['MicrosoftWindowsDesktop', 'MicrosoftWindowsServer']),
                'offer': "Windows-{}".format(self.random.choice(['10', '7', '8'])),
                'license': self.random.choice(['Windows_Client', 'Windows_Server'])
            }
        else:
            return_dict = {
                'os': os_type,
                'publisher': self.random.choice(['OpenLogic', 'RedHat', 'Canonical']),
                'offer': self.random.choice(['CentOS-7.5', 'Debian-8']),
                'license': self.random.choice(['Linux_Client', 'Linux_Server'])
            }
        return return_dict

    def get(self):
        """Returns a dictionary containing properties for an Azure VM

        Returns:
            dict: Contains an object containing all Azure VM detailed properties
        """
        unique_ids = self.__get_unique_ids()
        os_type = self.__os_type()
        return_dict = {}
        computer_name = Computer().name
        resource_group_name = '{}_{}_{}'.format(self.random.choice(self.word_list), self.random.choice(self.word_list), self.random.choice(self.word_list))
        os_disk_name = "{}_OsDisk_1_{}".format(computer_name, self.uuid.uuid4().hex)
        return_dict['name'] = computer_name
        return_dict['resourceGroupName'] = resource_group_name
        return_dict['id'] = "/subscriptions/{sub_id}/resourceGroups/{rgn}/providers/Microsoft.Compute/virtualMachines/{name}".format(
            sub_id=unique_ids['subscription_id'],
            rgn=resource_group_name,
            name=computer_name
        )
        return_dict['type'] = 'Microsoft.Compute/virtualMachines'
        return_dict['location'] = self.random.choice(self.__LOCATION_LIST)
        return_dict['properties'] = {
          'vmId': unique_ids['vm_id'],
          'hardwareProfile': {
            'vmSize': self.random.choice(self.__SIZE_LIST)
          }
        }
        return_dict['storageProfile'] = {
          "imageReference": {
            "publisher": os_type['publisher'],
            "offer": os_type['offer'],
            "sku": "rs5-pro",
            "version": "latest"
          },
          "osDisk": {
            "osType": os_type['os'],
            "name": os_disk_name,
            "createOption": "FromImage",
            "caching": "ReadWrite",
            "managedDisk": {
              "storageAccountType": "Premium_LRS",
              "id": "/subscriptions/{sub_id}/resourceGroups/{rgn}/providers/Microsoft.Compute/disks/{disk}".format(
                sub_id=unique_ids['subscription_id'], 
                rgn=resource_group_name, 
                disk=os_disk_name)
            },
            "diskSizeGB": 127
          },
          "dataDisks": []
        }
        return_dict['osProfile'] = {
          "computerName": computer_name,
          "adminUsername": "swimlane",
          "windowsConfiguration": {
            "provisionVMAgent": self.random.choice(['true', 'false']),
            "enableAutomaticUpdates": self.random.choice(['true', 'false'])
          },
          "secrets": [],
          "allowExtensionOperations": self.random.choice(['true', 'false']),
          "requireGuestProvisionSignal": self.random.choice(['true', 'false'])
        }
        return_dict['networkProfile'] = {
          'networkInterfaces': [{
            'id': "/subscriptions/{sub_id}/resourceGroups/{rgn}/providers/Microsoft.Network/networkInterfaces/{name}{count}".format(sub_id=unique_ids['subscription_id'], rgn=resource_group_name, name=computer_name, count=self.random.randint(500,1000))
          }]
        }
        return_dict['diagnosticsProfile'] = {
          "bootDiagnostics": {
            "enabled": self.random.choice(['true', 'false']),
            "storageUri": "https://{rgn}dia125.blob.core.windows.net/".format(
              rgn=resource_group_name.replace('_',''))
          }
        }
        return_dict['licenseType'] = os_type['license']
        return_dict['provisioningState'] = 'Succeeded'
        return return_dict
