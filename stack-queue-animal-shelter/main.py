from Animal import Animal
from Animal_shelter import AnimalShelter

# create an animal shelter
shelter = AnimalShelter()

# add animals to the shelter
shelter.enqueue(Animal("Max", "dog"))
shelter.enqueue(Animal("Meshmesh", "dog"))
shelter.enqueue(Animal("Fluffy", "cat"))
shelter.enqueue(Animal("Tom", "cat")) #tom and jerry :D

# adopt a dog
adopted_dog = shelter.dequeue("dog")
if adopted_dog:
    print(f"Congratulations! You have adopted {adopted_dog.name}, a {adopted_dog.species}.")
else:
    print("Sorry, there are no dogs available for adoption.")

    
# adopt a dog
adopted_dog = shelter.dequeue("dog")
if adopted_dog:
    print(f"Congratulations! You have adopted {adopted_dog.name}, a {adopted_dog.species}.")
else:
    print("Sorry, there are no dogs available for adoption.")

# adopt a dog
adopted_dog = shelter.dequeue("dog")
if adopted_dog:
    print(f"Congratulations! You have adopted {adopted_dog.name}, a {adopted_dog.species}.")
else:
    print("Sorry, there are no dogs available for adoption.")



# adopt a cat
adopted_cat = shelter.dequeue("cat")
if adopted_cat:
    print(f"Congratulations! You have adopted {adopted_cat.name}, a {adopted_cat.species}.")
else:
    print("Sorry, there are no cats available for adoption.")



# adopt a cat
adopted_cat = shelter.dequeue("cat")
if adopted_cat:
    print(f"Congratulations! You have adopted {adopted_cat.name}, a {adopted_cat.species}.")
else:
    print("Sorry, there are no cats available for adoption.")


# adopt a cat
adopted_cat = shelter.dequeue("cat")
if adopted_cat:
    print(f"Congratulations! You have adopted {adopted_cat.name}, a {adopted_cat.species}.")
else:
    print("Sorry, there are no cats available for adoption.")

