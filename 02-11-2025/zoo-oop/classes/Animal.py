class Animal:
    isMammal: bool 
    IsHungry: bool
    name : str
    Age : int
    isPredator: bool

    def __init__(self, name: str, Age: int, isMammal: bool, IsHungry: bool, isPredator: bool):
        self.name = name
        self.Age = Age
        self.isMammal = isMammal
        self.IsHungry = IsHungry
        self.isPredator = isPredator