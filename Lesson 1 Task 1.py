## Objects and references
# Task 1 (The Fastest car)


class Car:
    def __init__(self,make:str,top_speed:int):
        self.make = make
        self.top_speed = top_speed

def fastest_car(cars:list):
    speed = 0
    car = ''
    for i in cars:
        if i.top_speed > speed:
            speed = i.top_speed
            car = i.make
    return car
        
    
if __name__ == "__main__":
    car1 = Car("Saab", 195)
    car2 = Car("Lada", 110)
    car3 = Car("Ferrari", 280)
    car4 = Car("Trabant", 85)

    cars = [car1, car2, car3, car4]
    print(fastest_car(cars))
