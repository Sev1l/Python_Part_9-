## Objects as attributes
# Task 1 (Pets)

class Pet:
    def __init__(self,name,kind):
        self.name = name
        self.kind = kind

class Person:
    def __init__(self,name, pet: Pet):
        self.name = name
        self.pet = pet
    def __str__(self):
        return(f'{self.name}, whose pal is {self.pet.name}, a {self.pet.kind}')




hulda = Pet("Hulda", "mixed-breed dog")
levi = Person("Levi", hulda)

print(levi)


