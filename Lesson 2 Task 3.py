## Objects as attributes
# Task 3 (The shortest person in the room)


class Person:
    def __init__(self,name,height):
        self.name = name
        self.height = height

class Room:
    def __init__(self):
        self.number = 0
        self.room = []
    def add(self,person: Person):
        self.room += [person]
        self.number += 1

    def is_empty(self):
        if self.number == 0:
            return True
        else:
            return False

    

    def shortest(self):
        if self.number == 0:
            return None
        else:
            for person in self.room:
                self.cm = person.height
                self.who = person.name
                break
            for person in self.room:
                if person.height < self.cm:
                    self.cm = person.height
                    self.who = person.name
            return self.who
    def remove_shortest(self):
        if self.number == 0:
            return None
        else:
            self.new_list = []
            for person in self.room:
                if person.name != self.who:
                    self.new_list += [person]
            for person in self.room:
                if person.name == self.who:
                    return person
    def print_contents(self):
        self.summ = 0
        self.total_height = 0
        for person in self.new_list:
            self.summ += 1
            self.total_height += person.height
            
        print(f'There are {self.summ} persons in the room, and their combined height is {self.total_height} cm')
        for person in self.new_list:
            print(f'{person.name} ({person.height} cm)')
            

room = Room()
print("Is the room empty?", room.is_empty())
print("Shortest:", room.shortest())
room.add(Person("Lea", 183))
room.add(Person("Kenya", 172))
room.add(Person("Ally", 166))
room.add(Person("Nina", 162))

print()

print("Is the room empty?", room.is_empty())
print("Shortest:", room.shortest())

print()

removed = room.remove_shortest()
print(f"Removed from room: {removed.name}")

print()

room.print_contents()
