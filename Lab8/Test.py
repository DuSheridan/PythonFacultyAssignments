import unittest
from Lab8.Clasa import Complex


class TestComplex(unittest.TestCase):
    def setUp(self):
        self.__complex = Complex(3, 4)
        self.__complex2 = Complex(-3, -4)

    def test__complex(self):
        assert self.__complex.getReal() == 3
        assert self.__complex == Complex(3, 4)
        assert self.__complex.conjugat() == Complex(3, -4)
        assert self.__complex.modul()==5
        assert self.__complex.expo()==Complex(-13.13,-15.2)
        assert self.__complex+Complex(7,6)==Complex(10,10)
        assert self.__complex*Complex(1,0)==Complex(3,4)
        assert (self.__complex.radicalcomplex() == Complex(2.0, 1.0))
        assert self.__complex2.getReal() == -3
        assert self.__complex2 == Complex(-3, -4)
        assert self.__complex2.conjugat() == Complex(-3, 4)
        assert self.__complex2.modul() == 5
        print(self.__complex.polare())
        assert (self.__complex.theta() == 53.13)
        self.__complex.setReal(-3)
        assert self.__complex.getReal() == -3
        assert self.__complex == Complex(-3, 4)
        assert self.__complex.conjugat() == Complex(-3, -4)
        assert self.__complex.modul() == 5
        print(self.__complex.polare())
        self.__complex.setReal(3)
        assert(self.__complex*Complex(1,0)==Complex(3,4))
        '''
        print(str(self.__complex))
        print((self.__complex*Complex(1,0)))
        print(self.__complex.putere(3))
        print(self.__complex.reprezmat())
        print(self.__complex.radicalcomplex())
        print(self.__complex.theta())
        print(self.__complex.cart())
        print(self.__complex.expo())
        '''
    def test__complex2(self):
        self.__complex2.setReal(0)
        self.__complex2.setImag(0)
        assert self.__complex2.getReal() == 0
        assert self.__complex2 == Complex(0, 0)
        assert self.__complex2.conjugat() == Complex(0, 0)
        assert self.__complex2.modul() == 0
        assert self.__complex2.expo() == Complex(1, 0)
        assert self.__complex2 + Complex(7, 6) == Complex(7, 6)
        assert self.__complex2 * Complex(1, 0) == Complex(0, 0)
        assert (self.__complex2.radicalcomplex() == Complex(0, 0))

if __name__ == '__main__':
    unittest.main()


