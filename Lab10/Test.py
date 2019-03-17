import unittest
from Lab10.Clasa import Produs

class Test (unittest.TestCase):
    def setUp(self):
        self.__produs=Produs('Lapte','Lactate',200)

    def test__produs(self):
        assert(self.__produs.getDenum()=='Lapte')
        assert(self.__produs.getPrice()==200)
        assert(self.__produs.getType()=='Lactate')



if __name__=='__main__':
    unittest.main()