class AlienVault:

    @property
    def USM(self):
        from .alienvaultusm import AlienVaultUSM
        return AlienVaultUSM()
