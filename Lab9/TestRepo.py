import unittest
from Lab9.Repo import Repo
from Lab9.Ctrl import ControllerPP
from Lab9.Validator import PasagerValidator
from Lab9.Validator import PlaneValidator
from Lab9.Passenger import Passenger
from Lab9.Plane import Plane

class TestController(unittest.TestCase):

    def setUp(self):
        PV = PasagerValidator()
        AV = PlaneValidator()
        repo=Repo()
        repo2= Repo()
        self.__ctrl = ControllerPP(repo, repo2, PasagerValidator, PlaneValidator)

    #Tests for controller
    def test__ctrl(self):
        pasager1=Passenger("Doamne", "Daniel", "1234")
        pasager2=Passenger("Daniel", "Doamne", "4321")
        self.__ctrl.pas_repo.add_repo(pasager1)

        avion = Plane("Of", "23536", "Air", 300, "Roma", [pasager1, pasager2])
        self.__ctrl.avion_repo.add_repo(avion)
        assert (self.__ctrl.avion_repo.getAll()[0]== avion)
        assert (self.__ctrl.pas_repo.getAll()[0] == pasager1)







if __name__=='__main__':
    unittest.main()


