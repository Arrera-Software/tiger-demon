from librairy.jsonWorkOnline import *
from librairy.dectectionOS import *
import requests

class CTigerDemon :
    def __init__(self,nameSoft : str,url :str):
        # Teste internet
        try:
            response = requests.get("https://www.google.com/", timeout=5)
            self.__internet = True
        except requests.RequestException:
            self.__internet = False
        # objet
        self.__system = OS()
        # load depots
        if self.__internet:
            depotFile = jsonWorkOnline()
            depotFile.loadInternet(url)
            # Chargement des informations du logiciel
            self.__dictSofts = depotFile.dictJson()[nameSoft]

    def checkUpdate(self):
        if self.__internet:
            versionInstalled = self.getVersionSoft()
            if (versionInstalled != "IXXXX-XXX"):
                versionOnline = self.__dictSofts["version"]
                if (versionInstalled != versionOnline):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return True

    def getVersionSoft(self):
        versionInstalled = ""
        with open("VERSION", "r") as fichier:
            for ligne in fichier:
                # Si la ligne commence par "VERSION="
                if ligne.startswith("VERSION="):
                    # Supprimer le saut de ligne éventuel et récupérer la valeur
                    version = ligne.strip().split("=")[1]
                    versionInstalled = version
            fichier.close()

        return versionInstalled

    def getInternet(self):
        return self.__internet
