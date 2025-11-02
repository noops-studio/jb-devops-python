from classes.Plan import Plan


class Flight:
    FlightNumber:str
    ActivePlane:Plan
    IsInFlight:bool

    def __init__(self, FlightNumber:str, ActivePlane:Plan, IsInFlight:bool):
        self.FlightNumber = FlightNumber
        self.ActivePlane = ActivePlane
        self.IsInFlight = IsInFlight
        
        
    def fly(self):
        if not self.IsInFlight:
            self.IsInFlight = True
            print(f"Flight {self.FlightNumber} is now in the air. whoosh woosh!")
        else:
            print(f"Flight {self.FlightNumber} is already in the air.")
    
    def land(self):
        if self.IsInFlight:
            self.IsInFlight = False
            print(f"Flight {self.FlightNumber} has landed.")
        else:
            print(f"Flight {self.FlightNumber} is already on the ground.")