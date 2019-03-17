from Lab9.Passenger import Passenger


class Plane:

    def __init__(self, name, number, company, number_of_seats, destination, passenger_list):
        self.name = name
        self.number = number
        self.company = company
        self.number_of_seats = number_of_seats
        self.destination = destination
        self.passenger_list = passenger_list

    def get_name(self):
        return self.name

    def get_number(self):
        return self.number

    def get_company(self):
        return self.company

    def get_number_of_seats(self):
        return self.number_of_seats

    def get_destination(self):
        return self.destination

    def get_passenger_list(self):
        return self.passenger_list

    def set_name(self, n):
        self.name = n

    def set_number(self, nr):
        self.number = nr

    def set_company(self, comp):
        self.company = comp

    def set_number_of_seats(self, nrloc):
        self.number_of_seats = nrloc

    def set_destination(self, dest):
        self.destination = dest

    def set_passenger_list(self, paslist):
        self.passenger_list = paslist

    # Def:Gets how many passengers have the same first_name_
    # initial as their first letter in their first_name
    # In:Plane(self) and first_name_initial(character)
    # Out:Number of passengers (int) who satisfy the condition
    def same_initial_passengers(self, first_name_initial):
        nr_passengers = 0
        for i in range(0, len(self.passenger_list)):
            if self.passenger_list[i].get_first_name()[0] == first_name_initial:
                nr_passengers += 1
        return nr_passengers

    # Def:Checks if there are any passengers with
    # the same 3 first digits in their serial numbers
    # In: Plane(self)
    # Out: Boolean true or false
    def passengers_with_similar_series(self):
        for i in range(0, len(self.passenger_list) - 1):
            for j in range(i+1, len(self.passenger_list)):
                if(self.passenger_list[i].get_serial_number()[0:3] == self.passenger_list[j].get_serial_number()[0:3]):
                    return True
        return False

    # Def:Checks if there are any passengers with the same last_name as given_last_name
    # In:Plane(self), given_last_name(string)
    # Out:True or false
    def is_name_on_plane(self, given_last_name):
        for i in self.passenger_list:
            if(i.get_last_name() == given_last_name):
                return True
        return False

    def __repr__(self):
        return "(" + str(self.name) + " " + str(self.number) + " " + str(self.company) + " " + str(self.number_of_seats) + " " + str(self.destination) + " " + str(self.passenger_list)

    def __str__(self):
        return "(" + str(self.name) + " " + str(self.number) + " " + str(self.company) + " " + str(self.number_of_seats) + " " + str(self.destination) + " " + str(self.passenger_list)

    def __eq__(self, other):
        return self.number == other.numar
