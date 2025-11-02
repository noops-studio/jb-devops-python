from classes.Animal import Animal
from classes.Cage import Cage

newAnimal = Animal("Lion", "Simba", 5, True, True, True)

print(f"Animal Name: {newAnimal.name}, Nickname: {newAnimal.Nickname}, Age: {newAnimal.Age}, Is Mammal: {newAnimal.isMammal}, Is Hungry: {newAnimal.IsHungry}, Is Predator: {newAnimal.isPredator}")

newCage = Cage("Cage 1")


print(f"Cage Number: {newCage.CageNumber}, Max Capacity: {newCage.MaxAnimalCapacity}, Is Clean: {newCage.IsClean}, Animals in Cage: {len(newCage.Animals)}")
newCage.Animals.append(newAnimal)
print(f"Animals in Cage after adding one: {len(newCage.Animals)}")