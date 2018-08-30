
from CoreGame.Menus.Model.Nav import NAV
from CoreGame import Settings

class ServNav():
    def __init__(self):
        self.arnavs = []
        self.mockupdata()

    def addnav(self,preco,vel,disp,life):
        self.arnavs.append(NAV(preco,vel,disp,life))

    def getnavs(self):
        return self.arnavs


    def mockupdata(self):
        self.addnav(250,10,10,10)
        self.addnav(450, 20, 20, 20)
        self.addnav(750, 30, 30, 30)
