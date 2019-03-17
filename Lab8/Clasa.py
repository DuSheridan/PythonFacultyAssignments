from numpy import sin
from numpy import cos
from numpy import sqrt
from numpy import arcsin
from numpy import degrees
from numpy import deg2rad
from numpy import exp


class Complex:
    def __init__(self, real=0, imag=0):
        #if (isinstance(real, str) or isinstance(imag , str)):
         #   raise ValueError("Not a number")
        if not(((isinstance(real,int)==True)or(isinstance(real,float)==True))and((isinstance(imag,int)==True)or(isinstance(imag,float)==True))):
            raise ValueError("Not a number")
        self.r = real
        self.i = imag

    def __str__(self):
        if (self.i < 0):
            return str(self.r) + str(self.i) + "i"
        else:
            return str(self.r) + "+" + str(self.i) + "i"

    def __eq__(self, other):
        return self.r == other.r and self.i == other.i

    def __add__(self, other):
        return Complex(self.r + other.r, self.i + other.i)

    def __mul__(self, other):
        return Complex((self.r * other.r - self.i * other.i), (self.i * other.r + self.r * other.i))

    def __rmul__(self, other):
        return Complex((self.r * other.r - self.i * other.i), (self.i * other.r + self.r * other.i))

    def getReal(self):
        return self.r

    def getImag(self):
        return self.i

    def setReal(self, real):
        self.r = real

    def setImag(self, imag):
        self.i = imag

    def conjugat(self):
        return Complex(self.r, -1 * self.i)

    def cart(self):
        return ("Real=" + str(self.r) + " Imaginar=" + str(self.i))

    def modul(self):
        return round(sqrt((self.r * self.r) + (self.i * self.i)), 2)

    def theta(self):
        if (self.modul() == 0):
            return 0
        return round(degrees(arcsin((self.i) / (self.modul()))), 2)

    def polare(self):
        return str(self.modul()) + "*(cos" + str(self.theta()) + "+isin" + str(self.theta()) + ")"

    def putere(self, p):
        if (p == 0):
            return Complex(1, 0)
        if (self.r == 0) and (self.i == 0):
            return Complex(0, 0)
        theta = self.theta() * p
        modul = self.modul() ** p
        return Complex(round((modul * cos(deg2rad(theta))), 2), round((modul * sin(deg2rad(theta))), 2))

    def radicalimag(self):
        return (sqrt(self.modul())) * sin(deg2rad(self.theta() / 2))

    def radicalreal(self):
        return sqrt(self.modul()) * cos(deg2rad(self.theta() / 2))

    """
    def radical2real(self):
        return sqrt((self.modul())*(self.sine()/2))
    def radical2imag(self):
        return sqrt((self.modul())*self.cosine()/2)
    def radical2complex(self):
        return Complex(round(self.radical2real(),2),round(self.radical2imag(),2))
    """

    def radicalcomplex(self):
        return Complex(round(self.radicalreal(), 2), round(self.radicalimag(), 2))

    def expo(self):
        modul = exp(self.r)
        theta = self.i
        return Complex(round(modul * cos(theta), 2), round(modul * sin(theta), 2))

    def reprezmat(self):
        l = (self.r, -1 * self.i)
        l2 = (self.i, self.r)
        return (l, l2)
