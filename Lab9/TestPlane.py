import unittest
from Lab9.Plane import Plane
from Lab9.Passenger import Passenger
class TestPlane(unittest.TestCase):
    def setUp(self):
        self.__avion=Plane("ABCD", 123, "Avia", 320, "Roma", [Passenger('Petru', 'Pavel', 123), Passenger('Petru', 'NuPavel', '124')])

    # Some plane tests
    def test__plane(self):
        assert self.__avion.get_name() == "ABCD"
        assert self.__avion.get_number() == 123
        assert self.__avion.get_company() == "Avia"
        assert self.__avion.get_number_of_seats() == 320
        assert self.__avion.get_destination() == "Roma"
        assert self.__avion.get_passenger_list() == [Passenger('Petru', 'Pavel', 123), Passenger('Petru', 'NuPavel', '124')]
        self.__avion.set_name("DCBA")
        self.__avion.set_number(321)
        self.__avion.set_company("Aiva")
        self.__avion.set_number_of_seats(230)
        self.__avion.set_destination("Amor")
        assert self.__avion.get_name() == "DCBA"
        assert self.__avion.get_number() == "321"
        assert self.__avion.get_company() == "Aiva"
        assert self.__avion.get_number_of_seats() == "230"
        assert self.__avion.get_destination() == "Amor"



if __name__=='__main__':
    unittest.main()
