class Produs:
    def __init__(self,denumire,tip,pret):
        self.denum=denumire
        self.type=tip
        self.price=pret

    def getDenum(self):
        return self.denum
    def getType(self):
        return self.type
    def getPrice(self):
        return self.price


