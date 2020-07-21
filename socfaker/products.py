class Products(object):

    """The Products class is the main entrypoint for all product related data within soc-faker

    Returns:
        Products: A class which contains properties about different security products
    """

    @property
    def azure(self):
        """Azure class contains properties related to Azure products

        Returns:
            Azure: Microsoft Azure object containing properties and methods for generating data about Microsoft Azure products and services
        """
        from .azure import Azure
        return Azure()

    @property
    def elastic(self):
        """Elastic class contains properties related to Elastic products

        Returns:
            Elastic: Elastic object containing properties and methods for generating data about Elastic products and services
        """
        from .elastic import Elastic
        return Elastic()

    @property
    def servicenow(self):
        """ServiceNow class contains properties related to ServiceNow products

        Returns:
            ServiceNow: ServiceNow object containing properties and methods for generating data about ServiceNow products and services
        """
        from .servicenow import ServiceNow
        return ServiceNow()

    @property
    def qualysguard(self):
        """QualysGuard class contains properties related to Azure products

        Returns:
            QualysGuard: QualysGuard object containing properties and methods for generating data about QualysGuard
        """
        from .qualysguard import QualysGuard
        return QualysGuard()
