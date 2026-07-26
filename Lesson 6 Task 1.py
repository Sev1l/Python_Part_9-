## More examples with classes
# Task 1 (Item, Suitcase and Cargo hold)


class Item:
    def __init__(self,name,weight):
        self.__name = name
        self.__weight = weight
    def name(self):
        return self.__name
    def weight(self):
        return self.__weight

    def __str__(self):
        return f'{self.__name} ({self.__weight} kg)'
    
class Suitcase:
    def __init__(self,max_weight):
        self.__max_weight = max_weight
        self.__count = 0
        self.__weight = 0
        self.__case = []

    def add_item(self,item):
        if self.__weight + item.weight() <= self.__max_weight:
            self.__case += [item]
            self.__count += 1
            self.__weight += item.weight()
        

    def __str__(self):
        if self.__count == 1:
            return f'{self.__count} item ({self.__weight} kg)'
        else:
            return f'{self.__count} items ({self.__weight} kg)'
    def print_items(self):
        for i in self.__case:
            print (f'{i.name()} ({i.weight()} kg)')

    def weight(self):
        return self.__weight

    def heaviest_item(self):
        if len(self.__case) == 0:
            return None
        else:
            for i in self.__case:
                heaviest = i
                break
            for i in self.__case:
                if heaviest.weight() < i.weight():
                    heaviest = i
            return heaviest
            
class CargoHold:
    def __init__(self,maxim):
        self.__maxim = maxim
        self.__number = 0
        self.__cargo = []
        
    def add_suitcase(self,suitcase):
        if self.__maxim - suitcase.weight() >= 0:
            self.__number += 1
            self.__maxim -= suitcase.weight()
            self.__cargo += [suitcase]
    def print_items(self):
        for i in self.__cargo:
            i.print_items()
            
        

    def __str__(self):
        return f'{self.__number} suitcases, space for {self.__maxim} kg'
        

book = Item("ABC Book", 2)
phone = Item("Nokia 3210", 1)
brick = Item("Brick", 4)

adas_suitcase = Suitcase(10)
adas_suitcase.add_item(book)
adas_suitcase.add_item(phone)

peters_suitcase = Suitcase(10)
peters_suitcase.add_item(brick)

cargo_hold = CargoHold(1000)
cargo_hold.add_suitcase(adas_suitcase)
cargo_hold.add_suitcase(peters_suitcase)

print("The suitcases in the cargo hold contain the following items:")
cargo_hold.print_items()
