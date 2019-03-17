from Lab14.Repo import Repo
from Lab14.Clasa import Participant
class Controller:
    def __init__(self, repo):
        self.repo = repo

    #Descr:Verifica daca numele si lista de numere sunt valide, le impacheteaza si le pune in lista repo
    #In:Self(Controller), Nume_participant, lista de numere
    #Out:None sau ValueError
    def add(self,nume_participant,lista_numere):
        if nume_participant == "" or nume_participant == None:
            raise ValueError("Nume participant invalid")
        if len(lista_numere) != 6:
            raise ValueError("Lista numere invalida")
        for i in range(0, len(lista_numere)):
            if(lista_numere[i]<1)or (lista_numere[i]>49):
                raise ValueError("Numere invalide")
        for i in range(0,len(lista_numere)):
            if not(isinstance(lista_numere[i],int)):
                raise ValueError("Numere Invalide")
        for i in range(0, len(lista_numere) - 1):

            for j in range(i+1, len(lista_numere)):
                if(lista_numere[i]==lista_numere[j]):
                    raise ValueError("Lista numere invalida")
        participant = Participant(nume_participant,lista_numere)
        self.repo.addrepo(participant)

    #Descr:Primeste o lista de numere bune si compara fiecare participant cu ea
    #In
    #Out
    def stergectrl(self, lista_numere_buna):
        lista_participanti = self.repo.getAll()
        for i in lista_participanti:
            bun = 0
            lista_numere = i.getLista()
            for numar in lista_numere:
                if(numar in lista_numere_buna):
                    bun = bun + 1
            if(bun < 3):
                self.repo.stergerepo(i.get_last_name())


    def premiu(self, lista_numere_buna, premiu):
        lista_participanti = self.repo.getAll()
        lista_bun = []
        for el in lista_participanti:
            bun = 0
            lista_numere = el.getLista()
            for numar in lista_numere:
                if(numar in lista_numere_buna):
                    bun = bun + 1
            lista_bun.append(bun)
        lista_nume_participanti_noua = []
        lista_suma_castigata = []
        for i in range(0,len(lista_participanti)):
            lista_nume_participanti_noua.append(lista_participanti[i].get_last_name())
            if(lista_bun[i] < 3):
                lista_suma_castigata.append(0)
            elif(lista_bun[i] == 3):
                castigatori = 0
                for i in range(0, len(lista_bun)):
                    if(lista_bun[i] == 3):
                        castigatori = castigatori + 1
                lista_suma_castigata.append((premiu/20)/castigatori)
            elif(lista_bun[i] == 4):
                castigatori = 0
                for i in range(0 , len(lista_bun)):
                    if(lista_bun[i] == 4):
                        castigatori = castigatori +1
                lista_suma_castigata.append((premiu/10)/castigatori)
            elif(lista_bun[i] == 5):
                castigatori = 0
                for i in range (0, len(lista_bun)):
                    if(lista_bun[i] == 5):
                        castigatori = castigatori + 1
                lista_suma_castigata.append(((premiu/10)*3)/castigatori)
            elif(lista_bun[i] == 6):
                castigatori = 0
                for i in range(0, len(lista_bun)):
                    if(lista_bun[i] == 6):
                        castigatori = castigatori +1
                lista_suma_castigata.append((premiu/castigatori))
        return lista_nume_participanti_noua, lista_suma_castigata

    def locul_unu(self, lista_numere_buna):
        lista_participanti = self.repo.getAll()
        lista_bun = []
        for el in lista_participanti:
            bun = 0
            lista_numere = el.getLista()
            for numar in lista_numere:
                if(numar in lista_numere_buna):
                   bun = bun + 1
            lista_bun.append(bun)
        lista_participanti_castigatori = []
        for i in range(0,len(lista_participanti)):
            if (lista_bun[i] == 6):
                lista_participanti_castigatori.append(lista_participanti[i].get_last_name())
        return lista_participanti_castigatori

    def getall(self):
        lista_participanti = self.repo.getAll()
        lista_nume = []
        lista_numere = []
        for i in lista_participanti:
            lista_nume.append(i.get_last_name())
            lista_numere.append(i.getLista())
        return lista_nume,lista_numere
