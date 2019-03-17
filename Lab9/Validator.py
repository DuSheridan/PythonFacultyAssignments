import re
from Lab9.Plane import Plane
from Lab9.Exceptii import PlaneException
from Lab9.Passenger import Passenger
from Lab9.Exceptii import PassengerException
class PlaneValidator:
    def __init__(self):
        pass

    def validator(self, c):
        errors = []
        nrloc = c.get_number_of_seats()
        if not(isinstance(nrloc, int))or (nrloc < 1):
            errors.append("Invalid number of seats")

        if(len (errors) > 0):
            raise PlaneException(str(errors))

class PasagerValidator:
    def __init__(self):
        pass

    def validate(self,x):
        errors=[]

        if(hasNumbers(x.get_last_name())):
            errors.append("Invalid last name")

        if(hasNumbers(x.get_first_name())):
            errors.append("Invalid first name")

        if(hascharacters(x.get_serial_number())):
            errors.append("Invalid serial number")

        if (len(x.get_serial_number()) == 0):
            errors.append("Serial number can't be 0")

        if(len(errors) > 0):
            raise PassengerException(str(errors))

    def validserie(self,x):
        errors=[]
        if(hascharacters(x.get_serial_number())):
            errors.append("Invalid serial number")
        if(len(x.get_serial_number())==0):
            errors.append("Invalid ")

        if(len(errors)>0):
            raise PassengerException(str(errors))

    def validprenume(self, x):
        errors=[]
        if(hasNumbers(x.get_first_name())):
            errors.append("Prenume invalid")
        if(len(errors) > 0):
            raise PassengerException(str(errors))

    def validnume(self, x):
        errors=[]
        if(hasNumbers(x.get_last_name())):
            errors,append("Nume invalid")
        if(len(errors) > 0):
            raise PassengerException(str(errors))

def hasNumbers(lista):
    return any(char.isdigit() for char in lista )


def hascharacters(lista):
    return re.search('[a-zA-Z]',lista)


