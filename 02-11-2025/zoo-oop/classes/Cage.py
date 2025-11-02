from classes.Animal import Animal
class Cage:
    Animals: list[Animal] = []
    CageNumber: str
    MaxAnimalCapacity: int = 4
    IsClean: bool = True

    def __init__(self, cage_number: str):
        self.CageNumber = cage_number
        self.Animals = []