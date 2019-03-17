class Passenger:

    def __init__(self,last_name,first_name,serial_number):
        self.last_name = last_name
        self.first_name = first_name
        self.serial_number = serial_number

    def get_last_name(self):
        return self.last_name

    def get_first_name(self):
        return self.first_name

    def get_serial_number(self):
        return self.serial_number

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_serial_number(self, serial_number):
        self.serial_number = serial_number

    #Def: Checks if string is contained in last_name or first_name
    #In: String, self(passenger)
    #Out: Boolean true or false
    def does_contain(self, string):
        if(string in self.last_name)or(string in self.first_name):
            return True
        return False

    def __repr__(self):
        return "Last Name: " + str(self.last_name) +\
               " First Name: " + str(self.first_name) +\
               " Serial Number: " + str(self.serial_number)

    def __str__(self):
        return "Last Name: " + str(self.last_name) +\
               " First Name: " + str(self.first_name)\
               + " Serial Number: " + str(self.serial_number)

    def __eq__(self,other):
        return self.serial_number == other.serie
