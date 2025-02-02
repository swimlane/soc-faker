from .baseclass import BaseClass

class CVES(BaseClass):
    """
    Randomly select CVE's from all_current_cves.txt
    """

    @property
    def cve(self):
        """
        return random selected CVE from thee file all_current_cves.txt
        """
        with open("./socfaker/data/cves/all_current_cves.txt","r") as txtFile:
            self.cves = txtFile.read().split("\n")
        return self.random.choice(self.cves)
