class AzureVM(object):

    __AZ_METRICS = None

    @property
    def details(self):
        from .azurevmdetails import AzureVMDetails
        return AzureVMDetails().get()

    @property
    def metrics(self):
        from .azurevmmetrics import AzureVMMetrics
        return AzureVMMetrics().get()

    @property
    def topology(self):
        from .azurevmtopology import AzureVMTopology
        return AzureVMTopology().get()