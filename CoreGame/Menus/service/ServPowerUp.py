from CoreGame.Menus.Model.PowerUp import PowerUp


class ServPowerUp():
    def __init__(self):
        self.arpw = []
        self.mockupdata()

    def addpw(self,image,valor,tipo):
        self.arpw.append(PowerUp(image,valor,tipo))

    def getpw(self):
        return self.arpw


    def mockupdata(self):
        self.addpw('lifeimg.png',5,0,100)
        self.addpw('lifeimg.png', 10, 0,200)
        self.addpw('lifeimg.png', 15, 0,300)
        self.addpw('velimg.png', 5, 1,100)
        self.addpw('velimg.png', 10, 1,200)
        self.addpw('velimg.png', 15, 1,300)
        self.addpw('shootimg.png', 5, 2,100)
        self.addpw('shootimg.png', 10, 2,200)
        self.addpw('shootimg.png', 15, 2,300)
