from Lab8.Clasa import Complex
def opafisare(a,b):

    c=Complex(a,b)
    return str(c)+"="+str(c.polare())

def opreprezcart(a,b):
    c=Complex(a,b)
    return c.cart()

def opreprezpolar(a,b):
    c=Complex(a,b)
    return c.polare()

def opconjugat(a,b):
    c=Complex(a,b)
    d=c.conjugat()
    return d.getReal(),d.getImag()

def opCxR(a,b,r):
    c=Complex(a,b)
    re=Complex(r,0)
    prod=c*re
    return prod.getReal(),prod.getImag()

def opCxI(a,b,i):
    c=Complex(a,b)
    im=Complex(0,i)
    prod=c*im
    return prod.getReal(),prod.getImag()


def opsumCC(a,b,c,d):
    e=Complex(a,b)
    f=Complex(c,d)
    sum=e+f
    return sum.getReal(),sum.getImag()

def opprodCC(a,b,c,d):
    e=Complex(a,b)
    f=Complex(c,d)
    prod=e*f
    return prod.getReal(),prod.getImag()

def opreprezmat(a,b):
    c=Complex(a,b)
    return c.reprezmat()

def oproot(a,b):
    c=Complex(a,b)
    d=c.radicalcomplex()
    return d.getReal(),d.getImag()

def oppow(a,b,p):
    c=Complex(a,b)
    d=c.putere(p)
    return d.getReal(),d.getImag()

def opexpo(a,b):
    c=Complex(a,b)
    d=c.expo()
    return d.getReal(),d.getImag()

