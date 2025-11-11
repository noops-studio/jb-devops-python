from Zoo.Animal import Animal
from Zoo.Cage import Cage
from Zoo.Food import Food
newAnimal = Animal("Zebra",True,False,21)
newCage = Cage("13FE")
newCage.AddAnimal(newAnimal)


newLion = Animal("Lion",True,True,15)
newMoose = Animal("Moose",True,False,99)

try:
    newMoose.feed(Food("Kartoshka",True))
    newLion.feed(Food("Svinya",False))
    newCage.AddAnimal(newLion)
except Exception as ex:
    print(ex)

print(f"Animal Name is {newAnimal.Name}")