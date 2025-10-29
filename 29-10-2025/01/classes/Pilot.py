from datetime import date



class Pilot:
    
    id:int 
    Fullname:str
    BirthDate:date
    Rank:str
    age:int
    def __init__(self, id:int, Fullname:str, BirthDate:date, Rank:str, age:int):
        self.id = id
        self.Fullname = Fullname
        self.BirthDate = BirthDate
        self.Rank = Rank
        self.age = age
        
        
class SuperPilot(Pilot):
    
    superPilotName:str