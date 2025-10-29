from classes.Passanger import Passenger


class Seat:
    id:int
    Row:int
    Column:str
    SeatClass:str
    PassengerSitting:Passenger

    def __init__(self, id:int, Row:int, Column:str, SeatClass:str, PassengerSitting:Passenger):
        self.id = id
        self.Row = Row
        self.Column = Column
        self.SeatClass = SeatClass
        self.PassengerSitting = PassengerSitting