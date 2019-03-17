from Lab9.Passenger import Passenger
from Lab9.Repo import Repo
from Lab9.Plane import Plane
from Lab9.Validator import PasagerValidator
from Lab9.Validator import PlaneValidator
from Lab9.Ctrl import ControllerPP
from Lab9.UI import UI
#Def:Starts the whole program
def app():
    rPass = Repo()
    rAvion = Repo()
    pasvalid = PasagerValidator()
    avvalid = PlaneValidator()
    ctrl = ControllerPP(rPass, rAvion, pasvalid, avvalid)
    ui = UI(ctrl)
    ui.run()

app()

