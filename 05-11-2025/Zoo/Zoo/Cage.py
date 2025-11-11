from Zoo.Animal import Animal
class Cage:
    Animals = []
    maxAnimalCapacity: int = 4
    CageID: str
    isClean: bool = True

    def __init__(self,_cageID:str):
        self.CageID=_cageID

    def AddAnimal(self,_animal:Animal):
        # Check if theres room left to add the animal
        if (len(self.Animals) >= self.maxAnimalCapacity):
            raise(Exception("There is no room left in the cage"))

        # check there are no preditors in the cage in case we insert a preditor
        for _animalItem in self.Animals:
            if (_animalItem.isPreditor):
                raise(Exception("There is a preditor in the cage"))
        
        if (len(self.Animals) >= 1 and _animal.isPreditor):
            raise(Exception("There is a non preditor animal in the cage, Cannot Add preditor"))
        
        self.Animals.append(_animal)