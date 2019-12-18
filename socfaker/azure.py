class Azure(object):

    @property
    def vm(self):
        from .azurevm import AzureVM
        return AzureVM()