from numpy import array
from numpy import sum
from numpy import prod
from numpy import mean
from numpy import nanmin
from numpy import nanmax
#Descr:Adunarea unui scalar la toate elementele vectorului(numpy)
#In:Un vector si un scalar
#Out:Vectorul rezultat
def listAddition(l,x):
    a=array(l)
    return list(a+x)

print(listAddition([1,2,3],2))

def test_listAddition():
    assert(listAddition([1,2,3],2)==[3,4,5])
    assert(listAddition([],2)==[])
    assert(listAddition([1,2,3],0)==[1,2,3])
    assert(listAddition([],0)==[])
    assert(listAddition([300,300,300],-299)==[1,1,1])

test_listAddition()
#Descr:Adunarea a doi vectori, element cu element(numpy)
#In:2 Vectori
#Out:Vectorul Suma

def listsAddition(l1,l2):
    if(len(l1)!=len(l2)):
        raise ValueError("Vectori au dimensiuni diferite")
    a=array(l1)
    b=array(l2)
    return list(a+b)
def test_listsAddition():
    assert(listsAddition([1,2,3],[1,2,3])==[2,4,6])
    assert(listsAddition([1],[3])==[4])
    assert(listsAddition([],[])==[])
    assert(listsAddition([-100,-200,-300],[100,200,300])==[0,0,0])
    assert(listsAddition([300,200,100],[-300,-200,-100])==[0,0,0])


test_listsAddition()

#Descr:Scaderea a doi vectori, al doilea din primul(numpy)
#In:2 Vectori
#Out:Vectorul diferenta
def listSubtraction(l1,l2):
    if(len(l1)!=len(l2)):
        raise ValueError("Dimensiuni diferite")
    a=array(l1)
    b=array(l2)
    return list(a-b)

def test_listSubtraction():
    assert(listSubtraction([1,2,3],[1,2,3])==[0,0,0])
    assert(listSubtraction([3,3,3],[1,1,1])==[2,2,2])
    assert(listSubtraction([3,3,3],[-3,-3,-3])==[6,6,6])
    assert(listSubtraction([],[])==[])
    assert(listSubtraction([-3,-3,-3],[3,3,3])==[-6,-6,-6])

test_listSubtraction()

#Descr:Produsul scalar a 2 vectori(numpy)
#In:2 Vectori
#Out:Produsul scalar
def listsmultiplier(l1,l2):
    if(len(l1)!=len(l2)):
        raise ValueError("Dimensiuni diferite")
    a=array(l1)
    b=array(l2)
    return sum(a*b)

print(listsmultiplier([1,2,3],[4,5,5]))
def test_listsmultiplier():
    assert(listsmultiplier([1,2,3],[4,5,5])==29)
    assert(listsmultiplier([],[])==0)
    assert(listsmultiplier([1],[1])==1)
    assert(listsmultiplier([0,0,0],[0,0,0])==0)
    assert(listsmultiplier([1000,0,1],[0,1000,1])==1)
    print("All tests ok")

test_listsmultiplier()

#Descr:Suma elementelor listei date(numpy)
#In:Lista
#Out:Elementul suma
def listSum(l1):
    return sum(l1)

def test_listSum():
    assert(listSum([1,2,3])==6)
    assert(listSum([])==0)
    assert(listSum([3,3,3])==9)
    assert(listSum([0,0,0])==0)
    assert(listSum([100])==100)

test_listSum()

#Descr:Calculeaza produsul elementelor unei liste(numpy)
#In:Lista
#Out:Produsul
def listproduct(l1):
    return prod(l1)

def test_listproduct():
    assert(listproduct([1,2,3])==6)
    assert(listproduct([300,0,300])==0)
    assert(listproduct([0,0,0])==0)
    assert(listproduct([])==1)
    assert(listproduct([-1,-1,2])==2)

test_listproduct()

#Descr:Calculeaza media aritmetica a elementelor dintr-o lista(numpy)
#In:Lista
#Out:Media aritmetica
def listmean(l1):
    if(len(l1)==0):
        raise ValueError("Vector Nul")
    return mean(l1)

def test_listmean():
    assert(listmean([1,2,3])==2)
    assert(listmean([2,2,2])==2)
    assert(listmean([2])==2)
    assert(listmean([-3])==-3)
    assert(listmean([-2,-2,-2])==-2)

test_listmean()

#Descr:Minimul unei liste(numpy)
#In:Lista
#Out:Minimul
def listsmallest(l1):
    if(len(l1)==0):
        raise ValueError("Vector Nul")
    return nanmin(l1)

def test_listsmallest():
    assert(listsmallest([1,2,3])==1)
    assert(listsmallest([-100])==-100)
    assert(listsmallest([0])==0)
    assert(listsmallest([-100,-20,0])==-100)
    assert(listsmallest([1,2])==1)

test_listsmallest()

#Descr:Maximul unei liste (numpy)
#In:Lista
#Out:Maximul
def listlargest(l1):
    if(len(l1)==0):
        raise ValueError("Vector Nul")
    return nanmax(l1)

def test_listlargest():
    assert(listlargest([1,2,3])==3)
    assert(listlargest([0])==0)
    assert(listlargest([-100,0,100])==100)
    assert(listlargest([0,200])==200)
    assert(listlargest([100,0,-100])==100)

test_listlargest()


