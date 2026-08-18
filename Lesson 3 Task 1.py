## Encapsulation
# Task 1 (Car)


# Task 1 (Car)
class Car:
    def __init__(self):
        self.km = 0
        self.fuel = 0

    def fill_up(self):
        self.fuel = min(self.fuel + 60, 60)

    def drive(self, km):
        actual = min(km, self.fuel)
        self.km += actual
        self.fuel -= actual

    def __str__(self):
        return f'Car: odometer reading {self.km} km, petrol remaining {self.fuel} litres'


car = Car()
print(car)
car.fill_up()
print(car)
car.drive(20)
print(car)
car.drive(50)
print(car)
car.drive(10)
print(car)
car.fill_up()
car.fill_up()
print(car)
