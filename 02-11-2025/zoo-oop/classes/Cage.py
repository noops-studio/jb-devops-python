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
        # Check if cage has capacity
        if len(self.Animals) >= self.MaxAnimalCapacity:
            raise Exception("Cage is at full capacity")
            
        # Check if mixing predators and non-predators
        if len(self.Animals) > 0:
            # If adding a predator, check if there are non-predators in cage
            if animal.isPredator and any(not a.isPredator for a in self.Animals):
                raise Exception("Cannot add predator to cage with non-predators")
            
            # If adding a non-predator, check if there are predators in cage
            if not animal.isPredator and any(a.isPredator for a in self.Animals):
                predator = next(a for a in self.Animals if a.isPredator)
                raise Exception(f"Oh no! 😱 {predator.name} aka {predator.Nickname} just turned {animal.name} aka {animal.Nickname} into a three-course meal! 🍽️💀")
                
            
        
        self.Animals.append(animal)
        return True
    
    def get_animals(self) -> list[Animal]:
        return self.Animals
    
    
    def print_animals(self) -> None:
        for animal in self.Animals:
            print(f" - {animal.name} ({animal.Nickname})")