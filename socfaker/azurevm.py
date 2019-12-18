class AzureVM(object):

    __AZ_METRICS = None

    @property
    def details(self):
        from .azurevmdetails import AzureVMDetails
        return AzureVMDetails().get()

    @property
    def metrics(self):
        from .azurevmmetrics import AzureVMMetrics
        if not self.__AZ_METRICS:
            self.__AZ_METRICS = AzureVMMetrics()
            return self.__AZ_METRICS.get()
        return self.__AZ_METRICS

    @property
    def topology(self):
        from .azurevmtopology import AzureVMTopology
        return AzureVMTopology().get()