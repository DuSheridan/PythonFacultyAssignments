import ListOP as l
def citire():
    l=[]
    n=int(input("Nr de elemente al listei este="))
    for i in range(0,n):
        x=int(input("Elementul listei este "))
        l.append(x)
    return l

def uilistaddition():
    l1=citire()
    x=int(input("Scalarul pe care vreti sa-l adunati vectorului este"))
    print(l.listAddition(l1,x))

def uilistsAddition():
    l1=citire()
    l2=citire()
    print(l.listsAddition(l1,l2))

def uilistssubtraction():
    l1=citire()
    l2=citire()
    print(l.listSubtraction(l1,l2))

def uilistsproduct():
    l1=citire()
    l2=citire()
    print(l.listsmultiplier(l1,l2))

def uilistsum():
    l1=citire()
    print(l.listSum(l1))

def uilistproduct():
    l1=citire()
    print(l.listproduct(l1))

def uilistmean():
    l1=citire()
    print(l.listmean(l1))

def uilistsmallest():
    l1=citire()
    print(l.listsmallest(l1))

def uilistlargest():
    l1=citire()
    print(l.listlargest(l1))


def run():
    optiune=-1
    while(optiune!=0):
        print("0.Exit")
        print("1.Adunarea unui scalar la vector")
        print("2.Adunarea a doi vectori")
        print("3.Scaderea a doi vectori")
        print("4.Inmultirea scalara a doi vectori")
        print("5.Suma elementelor unui vector")
        print("6.Produsul elementelor unui vector")
        print("7.Media elementelor unui vector")
        print("8.Cel mai mic element a unui vector")
        print("9.Cel mai mare element a unui vector")
        optiune=int(input("Optiunea este "))
        if(optiune==1):
            uilistaddition()
            y=-1
            while(y!=10):
                y=int(input("Introduce-ti 10 pentru a continua "))
        elif(optiune==2):
            try:
                uilistsAddition()
                y=-1
                while(y!=10):
                    y=int(input("Introduce-ti 10 pentru a continua "))
            except ValueError as er:
                print("Something went wrong...:"+str(er))

        elif(optiune==3):
            try:

                uilistssubtraction()
                y=-1
                while(y!=10):
                    y=int(input("Introduce-ti 10 pentru a continua "))
            except ValueError as er:
                print("Something went wrong...:" + str(er))

        elif(optiune==4):
            try:
                uilistsproduct()
                y=-1
                while(y!=10):
                    y=int(input("Introduce-ti 10 pentru a continua "))
            except ValueError as er:
                print("Something went wrong...:" + str(er))

        elif(optiune==5):
            try:
                uilistsum()
                y = -1
                while (y != 10):
                    y = int(input("Introduce-ti 10 pentru a continua "))
            except ValueError as er:
                print("Something went wrong...:" + str(er))
        elif(optiune==6):
            try:
                uilistproduct()
                y = -1
                while (y != 10):
                    y = int(input("Introduce-ti 10 pentru a continua "))
            except ValueError as er:
                print("Something went wrong...:" + str(er))
        elif(optiune==7):
            try:
                uilistmean()
                y = -1
                while (y != 10):
                    y = int(input("Introduce-ti 10 pentru a continua "))
            except ValueError as er:
                print("Something went wrong...:" + str(er))
        elif(optiune==8):
            try:
                uilistsmallest()
                y = -1
                while (y != 10):
                    y = int(input("Introduce-ti 10 pentru a continua "))
            except ValueError as er:
                print("Something went wrong...:" + str(er))
        elif(optiune==9):
            try:
                uilistlargest()
                y = -1
                while (y != 10):
                    y = int(input("Introduce-ti 10 pentru a continua "))
            except ValueError as er:
                print("Something went wrong...:" + str(er))
        elif(optiune==0):
            pass
        else:
            print("Introduce-ti o optiune valida")

run()
