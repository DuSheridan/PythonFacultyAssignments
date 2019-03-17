from Lab14.Clasa import Participant
class Repo:
    def __init__(self, l = [Participant("A",[1,2,3,7,49,21]),Participant("B",(1,2,3,4,23,21)),Participant("C",[3,4,5,32,33,2]),Participant("D",[31,32,33,34,35,36]),Participant("Nora",[4,34,45,2,3,10])]):
        self.lista = l

    def getAll(self):
        return self.lista

    def addrepo(self, obiect):
        self.lista.append(obiect)

    def searchrepo(self, nume):
        for i in range(0, len(self.lista)):
            if self.lista[i].getNume() == nume:
                return i
        raise ValueError("Object not found")

    def stergerepo(self, nume):
        for i in range(0, len(self.lista)):
            if self.lista[i].getNume() == nume:
                del self.lista[i]
                break