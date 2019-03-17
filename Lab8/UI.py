from Lab8.OP import opconjugat
from Lab8.OP import opCxI
from Lab8.OP import opCxR
from Lab8.OP import opexpo
from Lab8.OP import oppow
from Lab8.OP import opprodCC
from Lab8.OP import opreprezcart
from Lab8.OP import opreprezmat
from Lab8.OP import opreprezpolar
from Lab8.OP import oproot
from Lab8.OP import opsumCC
from Lab8.OP import opafisare
from Lab8.Misc import deschiderefisier

from Lab8.Clasa import Complex


def uicitirereal():
    a=float(input("Numar real="))
    return a
def uicitireimaginar():
    b=float(input("Numar imaginar"))
    return b
def uicitirecomplex():
    a = uicitirereal()
    b = uicitireimaginar()
    return a,b
def filecitirecomplex(y,numbers):
    a,y,numbers = filecitirenumar(y,numbers)
    b,y,numbers = filecitirenumar(y,numbers)
    return a,b,y,numbers
def filecitirenumar(y,numbers):
    if(y==0):
        #try:
        numbers=deschiderefisier()
        '''
        except FileNotFoundError as ex:
            print("some probs:"+str(ex))
        except IOError as ex:
            print("some probs:" + str(ex))
        except ValueError as ex:
            print("some probs:" + str(ex))
        '''
    if(len(numbers)==0):
        raise ValueError("Empty file")
    if(y>len(numbers)-1):
        raise EOFError("End of file")
    n=numbers[y]
    return n,y+1,numbers
def uireprezcart(y,numbers):
    opt=int(input("1 for input 2 for file"))
    if(opt==1):
        a,b=uicitirecomplex()
    else:
        a,b,y,numbers=filecitirecomplex(y,numbers)
    return opreprezcart(a,b),y,numbers

def uireprezpolar(y,numbers):
    opt = int(input("1 for input 2 for file"))
    if (opt == 1):
        a, b = uicitirecomplex()
    else:
        a, b, y, numbers = filecitirecomplex(y, numbers)
    return opreprezpolar(a,b),y,numbers
def uiconjugat(y,numbers):
    opt = int(input("1 for input 2 for file"))
    if (opt == 1):
        a, b = uicitirecomplex()
    else:
        a, b, y, numbers = filecitirecomplex(y, numbers)
    c,d=opconjugat(a, b)
    return c,d,y,numbers
def uiCxR(y,numbers):
    opt = int(input("1 for input 2 for file "))
    if (opt == 1):
        a, b = uicitirecomplex()
        c = uicitirereal()
    else:
        a, b, y, numbers = filecitirecomplex(y, numbers)
        c, y, numbers = filecitirenumar(y,numbers)
    d,e=opCxR(a,b,c)
    return d,e,y,numbers
def uiCxI(y,numbers):
    opt = int(input("1 for input 2 for file "))
    if (opt == 1):
        a, b = uicitirecomplex()
        c = uicitireimaginar()
    else:
        a, b, y, numbers = filecitirecomplex(y, numbers)
        c, y, numbers = filecitirenumar(y,numbers)

    d,e=opCxI(a, b, c)

    return d,e,y,numbers
def uisumCC(y,numbers):
    opt = int(input("1 for input 2 for file "))
    if (opt == 1):
        a, b = uicitirecomplex()
        c, d = uicitirecomplex()
    else:
        a, b, y, numbers = filecitirecomplex(y, numbers)
        c, d, y, numbers = filecitirecomplex(y, numbers)
    e,f=opsumCC(a, b, c, d)
    return e,f,y,numbers
def uiprodCC(y,numbers):
    opt = int(input("1 for input 2 for file "))
    if (opt == 1):
        a, b = uicitirecomplex()
        c, d = uicitirecomplex()
    else:
        a, b, y, numbers = filecitirecomplex(y, numbers)
        c, d, y, numbers = filecitirecomplex(y, numbers)
    e,f=opprodCC(a, b, c, d)
    return e,f,y,numbers
def uireprezmat(y,numbers):
    opt = int(input("1 for input 2 for file "))
    if (opt == 1):
        a, b = uicitirecomplex()
    else:
        a, b, y, numbers = filecitirecomplex(y, numbers)
    return opreprezmat(a,b),y,numbers
def uipow(y,numbers):
    opt = int(input("1 for input 2 for file "))
    if (opt == 1):
        a, b = uicitirecomplex()
    else:
        a, b, y, numbers = filecitirecomplex(y, numbers)
    p=int(input("Puterea= "))
    c,d=oppow(a, b, p)
    return c,d,y,numbers
def uiroot(y,numbers):
    opt = int(input("1 for input 2 for file "))
    if (opt == 1):
        a, b = uicitirecomplex()
    else:
        a, b, y, numbers = filecitirecomplex(y, numbers)
    c,d=oproot(a, b)
    return c,d,y,numbers
def uiexpo(y,numbers):
    opt = int(input("1 for input 2 for file "))
    if (opt == 1):
        a, b = uicitirecomplex()
    else:
        a, b, y, numbers = filecitirecomplex(y, numbers)
    c,d=opexpo(a, b)
    return c,d,y,numbers

def afisare(elem):
    opt = int(input("1 for screen output 2 for file output"))
    if(opt == 1):
        print(elem)
    elif(opt == 2):
        scriere_fisier(elem)

def uiafisare(a,b):
    opt = int(input("1 for screen output 2 for file output"))
    if(opt == 1):
        print(opafisare(a,b))
    elif(opt == 2):
        scriere_fisier(opafisare(a,b))

def scriere_fisier(elem):
    f = open("Afisare", "a+")
    f.write(elem)
    f.close()


try:
    c=Complex(1,2)
except ValueError as ve:
    print(ve)

def run():
    x=1
    while(x==1):

        print("1.Reprezentarea carteziana")
        print("2.Reprezentarea polara")
        print("3.Conjugat")
        print("4.Inmultirea cu un numar real")
        print("5.Inmultirea cu un numar imaginar")
        print("6.Adunarea a 2 numere complexe")
        print("7.Inmultirea a 2 numere complexe")
        print("8.Reprezentarea matriciala")
        print("9.Ridicarea la putere")
        print("10.Radical(de ordinul 2) dintr-un numar complex")
        print("11.Exponentiala unui numar complex")
        print("0.Return")

        opt = -1
        y=0
        numbers=[]
        #yalt=0
        #numbersalt=[]
        while(opt!=0):
            opt=int(input("Optiunea dorita este "))
            if(opt==1):
                try:
                    reprezcart,y,numbers=uireprezcart(y,numbers)
                    afisare(reprezcart)
                    #y=yalt
                    #numbers=numbersalt.copy()
                except ValueError as ex:
                    print("some problems:"+str(ex))
                except EOFError as ex:
                    print("some problems:"+str(ex))
            elif(opt==2):
                try:
                    reprezpolar,y,numbers=uireprezpolar(y,numbers)
                    afisare(reprezpolar)
                    #y=yalt
                    #numbers=numbersalt.copy()
                except EOFError as ex:
                    print("some problems:"+str(ex))
                except ValueError as ex:
                    print("some problems:"+str(ex))

            elif(opt==3):
                try:
                    a,b,y,numbers=uiconjugat(y,numbers)
                    uiafisare(a,b)
                    #y=yalt
                    #numbers=numbersalt.copy()
                except EOFError as ex:
                    print("some problems:"+str(ex))
                except ValueError as ex:
                    print("some problems:"+str(ex))
            elif(opt==4):
                try:
                    a,b,y,numbers=uiCxR(y,numbers)
                    #y=yalt
                    #numbers=numbersalt.copy()
                    uiafisare(a,b)
                except EOFError as ex:
                    print("some problems:"+str(ex))
                except ValueError as ex:
                    print("some problems:"+str(ex))
            elif(opt==5):
                try:
                    a,b,y,numbers=uiCxI(y,numbers)
                    uiafisare(a,b)
                except EOFError as ex:
                    print("some problems:"+str(ex))
                except ValueError as ex:
                    print("some problems:"+str(ex))
            elif(opt==6):
                try:
                    a,b,y,numbers=uisumCC(y,numbers)
                    uiafisare(a,b)
                except EOFError as ex:
                    print("some problems:"+str(ex))
                except ValueError as ex:
                    print("some problems:"+str(ex))

            elif(opt==7):
                try:
                    a,b,y,numbers=uiprodCC(y,numbers)
                    uiafisare(a,b)
                except EOFError as ex:
                    print("some problems:"+str(ex))
                except ValueError as ex:
                    print("some problems:"+str(ex))
            elif(opt==8):
                try:
                    a,y,numbers=uireprezmat(y,numbers)
                    print(a[0])
                    print(a[1])
                    #y=yalt
                    #numbers=numbersalt.copy()
                except EOFError as ex:
                    print("some problems:"+str(ex))
                except ValueError as ex:
                    print("some problems:"+str(ex))
            elif(opt==9):
                try:
                    a,b,y,numbers=uipow(y,numbers)
                    #y=yalt
                    #numbers=numbersalt.copy()
                    uiafisare(a,b)
                except EOFError as ex:
                    print("some problems:"+str(ex))
                except ValueError as ex:
                    print("some problems:"+str(ex))
            elif(opt==10):
                try:
                    a,b,y,numbers=uiroot(y,numbers)
                    #y=yalt
                    #numbers=numbersalt.copy()
                    uiafisare(a,b)
                except EOFError as ex:
                    print("some problems:"+str(ex))
                except ValueError as ex:
                    print("some problems:"+str(ex))
            elif(opt==11):
                try:
                    a,b,y,numbers=uiexpo(y, numbers)
                    #y=yalt
                    #numbers=numberalt.copy()
                    uiafisare(a,b)
                except EOFError as ex:
                    print("some problems:"+str(ex))
                except ValueError as ex:
                    print("some problems:"+str(ex))
            elif(opt==0):
                pass
            else:
                print("Optiune incorecta")
        print("0.Exit")
        print("1.Continua")
        x=int(input("Optiune="))


run()
