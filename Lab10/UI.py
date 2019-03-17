from Lab10.Repo import Supermarket
def construire () :
    l = Supermarket()
    return l.getAll()

def filter(l):
    pret = int(input("Pret minim"))
    tip=input("Tip dorit")
    l.listfilter(pret,tip)

def meanprice(l):
    print("pretul mediu=")
    print(l.mean())

def afisare(l):
    l.afisare()
def testfilter():
    assert(filter)

def main():
    l=construire()
    afisare(l)
    filter(l)
    meanprice(l)
    return 0

main()

