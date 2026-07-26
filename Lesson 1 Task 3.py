## Objects and references
# Task 3 (Baby Centre)

class Person:
    def __init__(self,name,x,y,weight):
        self.name = name
        self.weight = weight


class BabyCentre:
    final = 0
    def weigh(self, person: Person):
        # return the weight of the person passed as an argument
        self.final += 1
        return person.weight
    def feed(self, person: Person):
        person.weight += 1
    def weigh_ins(self):
        return(self.final)


baby_centre = BabyCentre()

eric = Person("Eric", 1, 110, 7)
peter = Person("Peter", 33, 176, 85)

print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")

baby_centre.weigh(eric)
baby_centre.weigh(eric)

print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")

baby_centre.weigh(eric)
baby_centre.weigh(eric)
baby_centre.weigh(eric)
baby_centre.weigh(eric)

print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")

