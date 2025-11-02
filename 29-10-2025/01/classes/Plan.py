from classes.Pilot import Pilot
from classes.Seat import Seat
from classes.Passanger import Passenger
from  typing import List


class Plan:
    Name:str
    FlightPilot:Pilot
    PlaneSeats:List[Seat] = []
    
    def __init__(self, Name:str, FlightPilot:Pilot):
        self.Name = Name
        self.FlightPilot = FlightPilot



    def boardPassengerSeat(self, passenger: Passenger, seat: Seat):
        self.PlaneSeats.append(seat)