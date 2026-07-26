## Encapsulation
# Task 1 (Car)


class Car:
    def __init__(self):
        self.km = 0
        self.l = 0
    def fill_up(self):
        self.l += 60
        if self.l > 60:
            self.l = 60

    def drive(self,km):
        if self.l >= km:
            self.km += km
            self.l -= km
        else:
            extra = km - self.l
            self.l = 0
            self.km += km - extra

    def __str__(self):
        return f'Car: odometer reading {self.km} km, petrol remaining {self.l} litres'

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
