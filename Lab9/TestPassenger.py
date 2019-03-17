import unittest
from Lab9.Passenger import Passenger
class TestPassenger(unittest.TestCase):
    def setUp(self):
        self.__pasager = Passenger("Monika", "Blank", '1234567')

    #Some passenger tests
    def test__passenger(self):
        assert self.__pasager.get_last_name() == "Monika"
        assert self.__pasager.get_first_name() == "Blank"
        assert self.__pasager.get_serial_number() == "1234567"
        self.__pasager.set_last_name("Antonio")
        self.__pasager.set_first_name("Zait")
        self.__pasager.set_serial_number("7654321")
        assert self.__pasager.get_last_name() == "Antonio"
        assert self.__pasager.get_first_name() == "Zait"
        assert self.__pasager.get_serial_number() == "7654321"


if __name__=='__main__':
    unittest.main()