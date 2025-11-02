from classes.Animal import Animal
class Cage:
    Animals: list[Animal] = []
    CageNumber: str
    MaxAnimalCapacity: int = 4
    IsClean: bool = True

    def __init__(self, cage_number: str):
        self.CageNumber = cage_number
        self.Animals = []
        
        
    def add_animal(self, animal: Animal) -> bool:
        # now we will check if there are also preditors and non preditors in the same cage
        if len(self.Animals) < self.MaxAnimalCapacity and (animal.isPredator and any(a.isPrey for a in self.Animals) or not animal.isPredator):
            self.Animals.append(animal)
            return True
        return False