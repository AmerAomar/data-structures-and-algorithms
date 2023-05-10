from Animal import Animal

class AnimalShelter:
    def __init__(self):
        self.dogs = []
        self.cats = []

    def enqueue(self, animal:Animal):
        if animal.species == "dog":
            self.dogs.append(animal)

        elif animal.species == "cat":
            self.cats.append(animal)    


    def dequeue(self, pref):
        if pref == "dog" and self.dogs:
            return self.dogs.pop(0)
        
        elif pref == "cat" and self.cats:
            return self.cats.pop(0)
        
        else:
            return None
   

