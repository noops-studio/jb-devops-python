from classes.Pilot import Pilot

class Plan:
    Name:str
    FlightPilot:Pilot
    
    def __init__(self, Name:str, FlightPilot:Pilot):
        self.Name = Name
        self.FlightPilot = FlightPilot 