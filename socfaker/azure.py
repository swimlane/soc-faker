class Azure(object):

    """The Azure class is the entry point for all things Microsoft Azure

    Returns:
        Azure: Returns an Azure object with nested properties 
               like AzureVM class
    """

    @property
    def vm(self):
        """Property to access details about an Azure VM

        Returns:
            AzureVM: Returns a AzureVM class object
        """
        from .azurevm import AzureVM
        return AzureVM()
