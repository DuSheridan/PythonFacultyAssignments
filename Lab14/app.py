from Lab14.UI import UI
from Lab14.Controller import Controller
from Lab14.Repo import Repo

def app():
    r = Repo()
    c = Controller(r)
    U = UI(c)
    U.run()

app()