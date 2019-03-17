from Lab14.Controller import Controller
class UI:
    def __init__(self, controller):
        self.controller = controller

    #Descr:Citeste de la tastatura un nume de participant si o lista de numere si le trimite mai departe in controller
    #In:Self(UI)
    #Out:None
    def add(self):
        try:
            nume_participant = input("Numele participantului este ")
            lista_numere = []
            inca = True
            while(inca):
                x = int(input("Introdu un numar"))
                lista_numere.append(x)
                inca_numar = int(input("Mai introduci? 1 pentru DA 2 pentru NU"))
                valid = False
                while(not valid):

                    if(inca_numar == 1):
                        valid = True
                        inca = True
                    elif(inca_numar == 2):
                        valid = True
                        inca = False
                    else:
                        valid = False
            self.controller.add(nume_participant,lista_numere)
        except ValueError as ex:
            print("Probleme:"+str(ex))

    #Descr:Citeste de la tastatura lista de numere bune si trimite mai departe in controller
    #In:Self(UI)
    #Out:None
    def sterge(self):
        lista_numere_buna = []
        for i in range(0,6):
            x = int(input("Numarul "+str(i+1)+" este"))
            lista_numere_buna.append(x)
        self.controller.stergectrl(lista_numere_buna)

    #Descr:Afiseaza lista de participanti si suma castigata de fiecare
    #In:Self(UI)
    #Out:None
    def premiu(self):
        lista_numere_buna = []
        for i in range(0,6):
            x = int(input("Numarul "+str(i+1)+" este"))
            lista_numere_buna.append(x)
        premiu = int(input("Suma premiu"))
        lista_nume,lista_suma_castigata = self.controller.premiu(lista_numere_buna,premiu)
        for i in range(0, len(lista_nume)):
            print(lista_nume[i])
            print(lista_suma_castigata[i])

    #Descr:Afiseaza lista de castigatori
    #In:Self(UI)
    #Out:None
    def locul_unu(self):
        lista_numere_buna = []
        for i in range(0,6):
            x = int(input("Numarul "+str(i+1)+" este"))
            lista_numere_buna.append(x)
        lista_participanti_castigatori = self.controller.locul_unu(lista_numere_buna)
        for el in lista_participanti_castigatori:
            print(el)

    #Descr:Afiseaza lista de participanti
    #In:Self(UI)
    #Out:None
    def getall(self):
        lista_nume,lista_numere = self.controller.getall()
        for i in range(0,len(lista_nume)):
            print(lista_nume[i])
            print(lista_numere[i])


    def run(self):
        opt = -1
        while(opt):
            print("1.Adaugarea in lista a unui participant")
            print("2.Eliminarea participantilor cu mai putin de 3 numere bune")
            print("3.Determinarea sumei castigate de fiecare participant")
            print("4.Determinarea castigatorilor concursului")
            print("5.Get all")
            print("6.")
            print("0.Exit")
            opt = int(input("Optiunea dorita este "))
            if(opt == 1):
                self.add()
            elif(opt == 2):
                self.sterge()
            elif(opt == 3):
                self.premiu()
            elif(opt == 4):
                self.locul_unu()
            elif(opt == 5):
                self.getall()
            elif(opt == 6):
                pass
            elif(opt == 0):
                pass
            else:
                print("Introdu o optiune valida")
