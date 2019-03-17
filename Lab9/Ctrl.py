from Lab9.Plane import Plane
from Lab9.Passenger import Passenger
from Lab9.Exceptii import PlaneException
from Lab9.Exceptii import PassengerException
from Lab9.Repo import Repo
from Lab9.Validator import PasagerValidator
from Lab9.Validator import PlaneValidator


class ControllerPP:

    def __init__(self, pasrepo, avionrepo, validpas, validavion):
        self.valid_avion=validavion
        self.avion_repo=avionrepo
        self.pas_repo=pasrepo
        self.valid_pas=validpas

    def ctrl_add_plane(self, nume, numar, companie, numarloc, destinatie, ln, lp, ls):
        """

        :param type: nume:
        :param numar:
        :param companie:
        :param numarloc:
        :param destinatie:
        :param ln:
        :param lp:
        :param ls:
        rtype: List[int]
        rtype: Pasager
        :return:
        """

        if(len(ln) == len(lp)) and (len(ln) == len(ls)):
            list = []
            for i in range(0, len(ln)):
                x = Passenger(ln[i], lp[i], ls[i])
                self.valid_pas.validate(x)
                list.append(x)
            avion = Plane(nume, numar, companie, numarloc, destinatie, list)
            self.valid_avion.validator(avion)
            self.avion_repo.add_repo(avion)

        else:
            raise PassengerException("Date invalide")


    def cautare_avion_Ctrl(self, numar):
        avion0 = Plane("", numar, "", "", "", "")
        p = self.avion_repo.search_repo(avion0)
        nume = self.avion_repo.getAll()[p].get_last_name()
        numar = self.avion_repo.getAll()[p].get_number()
        companie = self.avion_repo.getAll()[p].get_company()
        nrloc = self.avion_repo.getAll()[p].get_number_of_seats()
        destinatie = self.avion_repo.getAll()[p].get_destination()
        paslist = self.avion_repo.getAll()[p].get_passenger_list()
        nume_list = []
        prenume_list = []
        serie_list = []
        for i in range(0,len(paslist)):
            nume_list.append(paslist[i].get_last_name())
            prenume_list.append(paslist[i].get_first_name())
            serie_list.append(paslist[i].get_serial_number())
        return nume, numar, companie, nrloc, destinatie, nume_list, prenume_list, serie_list

    def stergere_avion_Ctrl(self, numar):
        avion0 = Plane("", numar, "", "", "", "")
        self.avion_repo.delete_object_repo(avion0)

    def actualizare_avion_nume_Ctrl(self,numar,nume_nou):
        avion0 = Plane("", numar, "", "", "", "")
        p = self.avion_repo.search_repo(avion0)
        self.avion_repo.getAll()[p].set_last_name(nume_nou)

    def actualizare_avion_numar_Ctrl(self,numar, numar_nou):
        avion0 = Plane("", numar, "", "", "", "")
        p = self.avion_repo.search_repo(avion0)
        self.avion_repo.getAll()[p].set_number(numar_nou)

    def actualizare_avion_companie_Ctrl(self,numar,comp_nou):
        avion0 = Plane("", numar, "", "", "", "")
        p = self.avion_repo.search_repo(avion0)
        self.avion_repo.getAll()[p].set_company(comp_nou)

    def actualizare_avion_nrloc_Ctrl(self, numar, nrloc_nou):
        avion0 = Plane("", numar, "", "", "", "")
        p = self.avion_repo.search_repo(avion0)
        self.avion_repo.getAll()[p].set_number_of_seats(nrloc_nou)

    def actualizare_avion_dest_Ctrl(self, numar, dest_nou):
        avion0 = Plane("", numar, "", "", "", "")
        p = self.avion_repo.search_repo(avion0)
        self.avion_repo.getAll()[p].set_destination(dest_nou)

    def actualizare_avion_paslist_Ctrl(self, numar, lista_nume, lista_prenume, lista_serie):
        avion0 = Plane("", numar, "", "", "", "")
        p = self.avion_repo.search_repo(avion0)
        paslist = []
        for i in range(0,len(lista_serie)):
            x=Passenger(lista_nume[i], lista_prenume[i], lista_serie[i])
            paslist.append(x)
        self.avion_repo.getAll()[p].set_passenger_list(paslist)

    def adaugare_Ctrl_pasager(self, nume, prenume, serie, numar_avion):
        avion0 = Plane("", numar_avion, "", "", "", "")
        poz = self.avion_repo.search_repo(avion0)
        pas_list = self.avion_repo.getAll()[poz].get_passenger_list()
        max_pas_list = self.avion_repo.getAll()[poz].get_number_of_seats()
        if (len(pas_list) + 1 > max_pas_list):
            raise ValueError("Prea multi pasageri")
        pasager = Passenger(nume, prenume, serie)
        self.valid_pas.validate(pasager)
        pas_list.append(pasager)
        self.avion_repo.getAll()[poz].set_passenger_list(pas_list)

    def actualizare_pasager_serie_Ctrl(self, serie, serie_noua, numar_avion):
        avion0 = Plane("", numar_avion, "", "", "", "")
        poz = self.avion_repo.search_repo(avion0)
        pas_list = self.avion_repo.getAll()[poz].get_passenger_list()
        pasager_tinta = Passenger("", "", serie)
        pasager0 = Passenger("", "", serie_noua)
        self.valid_pas.validserie(pasager0)
        poz_gasit = -1
        for i in range(0, len(pas_list)):
            if(pas_list[i] == pasager_tinta):
                poz_gasit = i
        if (poz_gasit == -1):
            raise ValueError("Pasagerul nu este in acest avion")
        pas_list[poz_gasit].set_serial_number(serie_noua)
        self.avion_repo.getAll()[poz].set_passenger_list(pas_list)


    def actualizare_pasager_nume_Ctrl(self, serie, nume_nou, numar_avion):
        avion0 = Plane("", numar_avion, "", "", "", "")
        p = self.avion_repo.search_repo(avion0)
        pasager0 = Passenger(nume_nou, "", serie)
        self.valid_pas.validnume(pasager0)
        pas_list = self.avion_repo.getAll()[p].get_passenger_list()
        poz_gasit = -1
        for i in range(0, len(pas_list)):
            if(pas_list[i] == pasager0):
                poz_gasit = i
        if(poz_gasit == -1):
            raise ValueError("Pasagerul nu este in acest avion")
        pas_list[poz_gasit].set_last_name(nume_nou)
        self.avion_repo.getAll()[p].set_passenger_list(pas_list)

    def actualizare_pasager_prenume_Ctrl(self, serie, prenume_nou, numar_avion):
        avion0 = Plane("", numar_avion, "", "", "", "")
        poz = self.avion_repo.search_repo(avion0)
        pasager0 = Passenger("", prenume_nou, serie)
        self.valid_pas.validprenume(pasager0)
        self.valid_pas.validserie(pasager0)
        pas_list = self.avion_repo.getAll()[poz].get_passenger_list()[:]
        poz_gasit = -1
        for i in range(0, len(pas_list)):
            if(pas_list[i] == pasager0):
                poz_gasit = i
        if (poz_gasit == -1):
            raise ValueError("Pasagerul nu este in acest avion")
        pas_list[poz_gasit].set_first_name(prenume_nou)
        self.avion_repo.getAll()[poz].set_passenger_list(pas_list)

    def searchpasager(self, serie, numar_avion):
        avion0 = Plane("", numar_avion, "", "", "", "")
        poz = self.avion_repo.search_repo(avion0)
        pas_list = self.avion_repo.getAll()[poz].get_passenger_list()
        pasager0 = Passenger('', '', serie)
        gasit = False
        pasager_gasit = 0
        for i in range(0, len(pas_list)):
            if(pas_list[i] == pasager0):
                pasager_gasit = pas_list[i]
                gasit = True
                break
        if(gasit == False):
            raise ValueError("Pasagerul nu este in acest avion")

        nume = pasager_gasit.getNume()
        prenume = pasager_gasit.getPrenume()
        serie = pasager_gasit.getSerie()
        return nume, prenume, serie

    def sterge_pasager_Ctrl(self, serie, numar_avion):
        avion0 = Plane("", numar_avion, "", "", "", "")
        p = self.avion_repo.search_repo(avion0)
        pas_list = self.avion_repo.getAll()[p].get_passenger_list()
        pasager0 = Passenger("", "", serie)
        gasit = False
        for i in range(0, len(pas_list)):
            if(pas_list[i] == pasager0):
                poz_gasit = i
                gasit = True
        if (gasit == False):
            raise ValueError("Pasagerul nu este in acest avion")
        del pas_list[p]
        self.avion_repo.getAll()[p].set_passenger_list(pas_list)


    def sortare_pasageri_nume(self, numar_avion):
        avion0 = Plane("", numar_avion, "", "", "", "")
        poz = self.avion_repo.search_repo(avion0)
        avion = self.avion_repo.getAll()[poz]
        lista_pasageri = avion.get_passenger_list()
        ControllerPP.sort(lista_pasageri, lambda x, y: x.get_last_name() > y.get_last_name())
        for i in lista_pasageri:
            print(i)

    def sortare_avioane_litera_prenume(self, litera_prenume):
        lista_avioane = self.avion_repo.getAll()
        ControllerPP.sort(lista_avioane, lambda x, y: x.same_initial_passengers(litera_prenume) > y.same_initial_passengers(litera_prenume))
        for i in lista_avioane:
            print(i)


    def sortare_avioane_nr_avion_pasageri(self):
        lista_avioane = self.avion_repo.getAll()
        ControllerPP.sort(lista_avioane, lambda x, y: (str(len(x.get_passenger_list())) + x.get_number()) > (str(len(y.get_passenger_list())) + y.get_number()))
        for i in lista_avioane:
            print(i)

    def cautare_avioane_serii(self):
        lista_avioane = self.avion_repo.getAll()
        lista_avioane_ok = ControllerPP.cautare(lista_avioane, lambda x: x.passengers_with_similar_series())
        for i in lista_avioane_ok:
            print (i)


    def cautare_pasager_contine_sir(self, numar_avion, sir):
        avion0 = Plane("", numar_avion, "", "", "", "")
        poz = self.avion_repo.search_repo(avion0)
        lista_pasageri = self.avion_repo.getAll()[poz].get_passenger_list()
        lista_pasageri_ok = ControllerPP.cautare(lista_pasageri, lambda x: x.does_contain(sir))
        for i in lista_pasageri_ok:
            print (i)


    def cautare_avion_contine_pasager_nume(self, nume_tinta):
        lista_avioane = self.avion_repo.getAll()
        lista_avioane_ok = ControllerPP.cautare(lista_avioane, lambda x: x.is_name_on_plane(nume_tinta))
        for i in lista_avioane_ok:
            print(i)

    def formare_grupuri_pasageri(self, k):
        fail = 0
        for i in range(0, len(self.avion_repo.getAll())):
            lista_pasageri = self.avion_repo.getAll()[i].get_passenger_list()
            if k <= len(lista_pasageri):
                for p in ControllerPP.permut_back(lista_pasageri, ControllerPP.pasisconsistent, ControllerPP.issolution, k):
                    print (p)
            else:
                fail = fail + 1
        if fail == len(self.avion_repo.getAll()):
            raise ValueError("Insuficienti pasageri in oricare avion")
    def formare_grupuri_avioane(self, k):

        lista_avioane = self.avion_repo.getAll()
        if k > len(lista_avioane):
            raise ValueError("Insuficiente avioane")
        for p in ControllerPP.permut_back(lista_avioane, ControllerPP.avisconsistent1, ControllerPP.issolution, k):
            print (p)

    def get_all_ctrl(self):
        l=self.avion_repo.getAll()
        for i in range(0, len(l)):
            print (l[i])

    @staticmethod
    def sort(lista, cmp_function):
        for i in range(0, len(lista)-1):
            for j in range(i+1, len(lista)):
                if(cmp_function(lista[i], lista[j])):
                    lista[i], lista[j] = lista[j], lista[i]

    @staticmethod
    def test():
        l = []
        for i in range(0,4):
            l.append({
                "nume": "Teo",
                "valoare": i
            })
        l[1]["nume"]="Daniel"
        l[3]["nume"]="X"
        ControllerPP.sort(l, lambda x, y: x["nume"] > y["nume"])
        print(l)

    @staticmethod
    def cautare(lista, conditie):
        lista_ok = []
        for i in lista:
            if (conditie(i)):
                lista_ok.append(i)

        return lista_ok

    @staticmethod
    def permut_back(lista,isConsistent,isSolution,n):
        k = 0
        solution = []
        solution.append(lista[0])
        l=0
        while (k >= 0):
            isSelected = False
            while ((isSelected == False) and (l < len(lista))):
                solution[k] = lista[l]
                l = l + 1
                isSelected = isConsistent(solution)
            if (isSelected == True):
                if (isSolution(solution, n) == True):
                    yield solution
                else:
                    k = k + 1
                    solution.append(lista[0])
                    l = 0
            else:
                del solution[k]
                k = k - 1
        return 0

    @staticmethod
    def avisconsistent1(solution):
        dest = solution[0].get_destination()
        for i in solution:
            if(dest != i.get_destination()):
                return False
        for i in range(0, len(solution)-1):
            comp = solution[i].get_company()
            for j in range(i+1, len(solution)):
                if(comp == solution[j].get_company()):
                    return False
        return True

    @staticmethod
    def pasisconsistent(solution):
        for i in range(0, len(solution)-1):
            nume = solution[i].get_last_name()
            for j in range(i+1, len(solution)):
                if(nume == solution[j].get_last_name()):
                    return False
        return True

    @staticmethod
    def issolution(solution, n):
        return len(solution) == n


ControllerPP.test()