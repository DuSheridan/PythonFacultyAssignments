class PlaneException(Exception):
    def __init__(self,msg):
        self.message = msg

    def __repr__(self):
        return self.message

    def __str__(self):
        return self.message


class PassengerException(Exception):
    def __init__(self,msg):
        self.message = msg

    def __repr__(self):
        return self.message

    def __str__(self):
        return self.message
