from Lab9.Ctrl import ControllerPP
from Lab9.Exceptii import PlaneException
from Lab9.Exceptii import PassengerException

class UI:
    def __init__(self, ctrlA):
        self.ctrlAvion=ctrlA

    def add_passenger_UI(self):
        try:
            nume, prenume, serie=read_passenger()
            numar_avion = input("numar avion tinta")
            self.ctrlAvion.adaugare_Ctrl_pasager(nume, prenume, serie, numar_avion)

        except PassengerException as ex:
            print("Problems: " + str(ex))
        except ValueError as ex:
            print("Problems: " + str(ex))

    def cauta_pasager_serie(self):
        try:
            numar_avion = input("numar avion tinta")
            serie=input("serie=")
            print(self.ctrlAvion.searchpasager(serie, numar_avion))

        except PassengerException as ex:
            print("Problems:"+str(ex))

        except ValueError as ex:
            print("Problems:"+str(ex))

    def actualizare_pasagerUI(self):
        try:
            while(True):
                opt = int(input("1 pentru serie, 2 pentru nume , 3 pentru prenume"))
                if (opt == 1):
                    self.actualizare_pasager_serie()
                    break
                elif (opt == 2):
                    self.actualizare_pasager_nume()
                    break
                elif (opt == 3):
                    self.actualizare_pasager_prenume()
                    break
        except ValueError as ex:
            print("Problems:"+str(ex))

    def actualizare_pasager_serie(self):
        numar_avion= input("numar avion tinta")
        serie = input ("seria tinta")
        serie_noua = input ("seria noua")
        self.ctrlAvion.actualizare_pasager_serie_Ctrl(serie, serie_noua, numar_avion)

    def actualizare_pasager_prenume(self):
        numar_avion = input("numar avion tinta")
        serie = input("seria tinta")
        prenume_nou = input ("prenume nou")
        self.ctrlAvion.actualizare_pasager_prenume_Ctrl(serie, prenume_nou, numar_avion)

    def actualizare_pasager_nume(self):
        numar_avion = input("numar avion tinta")
        serie = input("seria tinta")
        nume_nou = input ("nume nou")
        self.ctrlAvion.actualizare_pasager_nume_Ctrl(serie, nume_nou, numar_avion)

    def sterge_pasager_UI(self):
        try:
            numar_avion = input("numar avion tinta")
            serie = input ("seria tinta")
            self.ctrlAvion.sterge_pasager_Ctrl(serie, numar_avion)
        except ValueError as ex:
            print("Problems:"+str(ex))

    def get_all_UI(self):
        self.ctrlAvion.get_all_ctrl()

    def adaugare_avion_UI(self):
        try:
            nume = input("nume")
            numar = input("numar")
            companie = input("companie")
            numarloc = int(input("Numar de locuri="))
            destinatie = input("Destinatie")
            nrpasageri = int(input("Nr de pasageri="))
            if (nrpasageri > numarloc):
                raise PlaneException("Prea multi pasageri")
            listanume = []
            listaprenume = []
            listaserie = []
            for i in range(0, nrpasageri):
                x, y, z = read_passenger()
                listanume.append(x)
                listaprenume.append(y)
                listaserie.append(z)
            self.ctrlAvion.ctrl_add_plane(nume, numar, companie, numarloc, destinatie, listanume, listaprenume, listaserie)
        except PlaneException as ex:
            print("Problems:" + str(ex))
        except PassengerException as ex:
            print("Problems:" + str(ex))
        except ValueError as ex:
            print("Problems:" + str(ex))

    def cautare_avion_UI(self):
        try:
            numar = input("numar")
            print(self.ctrlAvion.cautare_avion_Ctrl(numar))


        except PlaneException as ex:
            print("problems:"+str(ex))

        except ValueError as ex:
            print("problems:"+str(ex))


    def stergere_avion_UI(self):
        try:
            numar = input("numar tinta")
            self.ctrlAvion.stergere_avion_Ctrl(numar)

        except ValueError as ex:
            print("Problems:"+str(ex))

    def actualizare_avion_UI(self):
        try:
            while(True):
                opt = int(input("1 pentru nume, 2 pentru numar, 3 pentru companie, 4 pentru numar locuri 5 pentru destinatie 6 pentru lista de pasageri"))
                if(opt == 1):
                    self.actualizare_avion_nume_UI()
                    break
                elif(opt == 2):
                    self.actualizare_avion_numar_UI()
                    break
                elif(opt == 3):
                    self.actualizare_avion_companie_UI()
                    break
                elif(opt == 4):
                    self.actualizare_avion_nrloc_UI()
                    break
                elif(opt == 5):
                    self.actualizare_avion_dest_UI()
                    break
                elif(opt == 6):
                    self.actualizare_avion_paslist_UI()
                    break
        except ValueError as ex:
            print("Problems:"+str(ex))


    def actualizare_avion_nume_UI(self):
        numar = input("numar tinta")
        nume_nou = input("nume")
        self.ctrlAvion.actualizare_avion_nume_Ctrl(numar, nume_nou)

    def actualizare_avion_numar_UI(self):
        numar = input("numar tinta")
        numar_nou = input("numar nou")
        self.ctrlAvion.actualizare_avion_numar_Ctrl(numar,numar_nou)

    def actualizare_avion_companie_UI(self):
        numar = input("numar tinta")
        companie_nou = input("compania noua")
        self.ctrlAvion.actualizare_avion_companie_Ctrl(numar,companie_nou)

    def actualizare_avion_nrloc_UI(self):
        numar = input("numar tinta")
        nrloc_nou = int(input("nrloc nou"))
        self.ctrlAvion.actualizare_avion_nrloc_Ctrl(numar, nrloc_nou)

    def actualizare_avion_dest_UI(self):
        numar = input("numar tinta")
        dest_nou = input("destinatie noua")
        self.ctrlAvion.actualizare_avion_dest_Ctrl(numar, dest_nou)

    def actualizare_avion_paslist_UI(self):
        try:
            numar = input("numar tinta")
            nrpasageri_nou = int(input("nr pasageri noi"))
            lista_nume = []
            lista_prenume = []
            lista_serie = []
            for i in range(0,nrpasageri_nou):
                x,y,z = read_passenger()
                lista_nume.append(x)
                lista_prenume.append(y)
                lista_serie.append(z)
            self.ctrlAvion.actualizare_avion_paslist_Ctrl(numar, lista_nume, lista_prenume, lista_serie)
        except PassengerException as ex:
            print("some probs:"+str(ex))

    def sortare_pasageri_nume(self):
        try:
            numar_avion = input("numar avion tinta")
            self.ctrlAvion.sortare_pasageri_nume(numar_avion)
        except ValueError as ex:
            print("Problems:"+str(ex))

    def sortare_avioane_litera_prenume(self):
        try:
            litera_prenume = input("Initiala prenumelui")
            self.ctrlAvion.sortare_avioane_litera_prenume(litera_prenume)

        except ValueError as ex:
            print("Problems:"+str(ex))

    def sortare_avioane_nr_avion_pasageri(self):
        try:
            self.ctrlAvion.sortare_avioane_nr_avion_pasageri()
        except ValueError as ex:
            print("Problems:"+str(ex))

    def cautare_avioane_serii(self):
        self.ctrlAvion.cautare_avioane_serii()

    def cautare_pasager_contine_sir(self):
        try:
            sir = input("Sirul de caractere care trebuie sa-l contina pasagerii")
            numar_avion = input("Numarul avionului in care cautati pasagerii")
            self.ctrlAvion.cautare_pasager_contine_sir(numar_avion, sir)
        except ValueError as ex:
            print("Problems:"+str(ex))

    def cautare_avion_contine_pasager_nume(self):
        nume_tinta = input("Numele cautat")
        self.ctrlAvion.cautare_avion_contine_pasager_nume(nume_tinta)

    def formare_grupuri_pasageri(self):
        try:
            k = int(input("Cati pasageri are un grup? "))
            self.ctrlAvion.formare_grupuri_pasageri(k)
        except ValueError as ex:
            print("probs:"+str(ex))

    def formare_grupuri_avioane(self):
        try:
            k = int(input("Cate avioane are un grup"))
            self.ctrlAvion.formare_grupuri_avioane(k)
        except ValueError as ex:
            print("probs:"+str(ex))
    def run(self):
        opt = -1
        while(opt!=0):
            print("0.Exit")
            print("1.Adaugare Pasager")
            print("2.Cauta Pasager")
            print("3.Actualizeaza Pasager")
            print("4.Stergere Pasager")
            print("5.Adaugare Avion")
            print("6.Cautare Avion")
            print("7.Actualizare Avion")
            print("8.Stergere Avion")
            print("9.Sortarea dupa nume a pasagerilor unui avion")
            print("10.Sortarea avioanelor in functie de numarul de pasageri ale caror prenume incepe cu o litera data")
            print("11.Sortarea avioanelor in functie de numarul de pasageri si numarul avionului")
            print("12.Cautarea avioanelor in care exista pasageri"
                  " care au serii de pasaport care incep cu aceleasi 3 caractere")
            print("13.Cautarea pasagerilor dintr-un avion dat al caror nume sau prenume contine un sir de caractere dat")
            print("14.Cautarea avioanelor in care se afla un pasager al carui nume este dar ca si parametru")
            print("15.Formarea de grupuri a cate k pasageri care zboara cu acelasi avion si au nume diferite")
            print("16.Formarea de grupuri a cate k avioane care au aceeasi destinatie si apartin unor companii aeriene diferite")
            print("17.Get all")
            opt = int(input("Optiunea dorita este"))
            if(opt == 1):
                self.add_passenger_UI()
            elif(opt == 2):
                self.cauta_pasager_serie()
            elif(opt == 3):
                self.actualizare_pasagerUI()
            elif(opt == 4):
                self.sterge_pasager_UI()
            elif(opt == 5):
                self.adaugare_avion_UI()
            elif(opt == 6):
                self.cautare_avion_UI()
            elif(opt == 7):
                self.actualizare_avion_UI()
            elif(opt == 8):
                self.stergere_avion_UI()
            elif(opt == 9):
                self.sortare_pasageri_nume()
            elif(opt == 10):
                self.sortare_avioane_litera_prenume()
            elif(opt == 11):
                self.sortare_avioane_nr_avion_pasageri()
            elif(opt == 12):
                self.cautare_avioane_serii()
            elif(opt == 13):
                self.cautare_pasager_contine_sir()
            elif(opt == 14):
                self.cautare_avion_contine_pasager_nume()
            elif(opt == 15):
                self.formare_grupuri_pasageri()
            elif(opt == 16):
                self.formare_grupuri_avioane()
            elif(opt == 17):
                self.get_all_UI()
            elif(opt == 0):
                pass
            else:
                print("Introdu o optiune valida")

def read_passenger():
    last_name = input("last_name=")
    first_name = input("first_name=")
    serial_number = input("serial_number=")
    return last_name,first_name,serial_number