from Lab10.Clasa import Produs

class Supermarket:
    def __init__(self):
        self.l=[Produs("Lapte","Lactate",200),Produs("Lion","Dulciuri",300),Produs("Snickers","Dulciuri",350)]

    def getAll(self):
        return self.l

    def listfilter(self,pret,tip):
        list=[]
        for i in range(0,len(self.l)):
            if(self.l[i].getPrice() > pret)and(self.l[i].getType()==tip):
                list.append(self.l[i])
        self.l=list.copy()

    def mean(self):
        pret=0
        for i in range(0,len(self.l)):
            pret=pret+self.l[i].getPrice()/len(self.l)
        return pret

    def afisare(self):
        listadenum=[]
        for i in range(0,len(self.l)):
            listadenum.append(self.l[i].getDenum())
        return listadenum


def main():
    l=Supermarket()
    print(l.afisare())
    pret=int(input("Pret"))
    tip=input("Tip")
    l.listfilter(pret,tip)
    print(l.afisare())
    print(l.mean())

def test_filtrare():
    l=Supermarket()
    l.listfilter(199,"Lactate")
    assert(len(l.afisare())==1)
    l=Supermarket()
    l.listfilter(340,"Dulciuri")
    assert(len(l.afisare())==1)
    l=Supermarket()
    l.listfilter(200,"OfDoamne")
    assert(len(l.afisare())==0)
    l=Supermarket()
    l.listfilter(3000,"Dulciuri")
    assert(len(l.afisare())==0)
    l=Supermarket()
    l.listfilter(199,"Dulciuri")
    assert (l.mean() ==325)
    assert(len(l.afisare())==2)
    l=Supermarket()
    print(l.mean())
    #assert(l.mean()==)
    print("all tests ok")
test_filtrare()

main()
