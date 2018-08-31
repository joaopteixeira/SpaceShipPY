




class PowerUp():
    def __init__(self,image,valor,tipo):
        self.image = image
        self.valor = valor
        self.tipo = tipo


    def getimage(self):
        return self.image

    def setimage(self,image):
        self.image = image

    def getvalor(self):
        return self.valor

    def setvalor(self, valor):
        self.valor = valor

    def gettipo(self):
        return self.tipo

    def settipo(self, tipo):
        self.tipo = tipo