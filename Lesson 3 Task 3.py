## Encapsulation
# Task 3 (Weather station)


class WeatherStation:
    def __init__(self,name):
        self.name = name
        self.list = []
        self.number = 0
    def add_observation(self,observation:str):
        self.list += [observation]
        self.number += 1

    def latest_observation(self):
        if len(self.list) == 0:
            return ''
        else:
            return self.list[len(self.list)-1]

    def number_of_observations(self):
        return self.number

    def __str__(self):
        return f'{self.name}, {self.number} observations'
        



station = WeatherStation("Houston")
station.add_observation("Rain 10mm")
station.add_observation("Sunny")
print(station.latest_observation())

station.add_observation("Thunderstorm")
print(station.latest_observation())

print(station.number_of_observations())
print(station)
