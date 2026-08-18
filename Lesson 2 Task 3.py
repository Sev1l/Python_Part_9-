## Objects as attributes
# Task 3 (The shortest person in the room)

class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height


class Room:
    def __init__(self):
        self.room = []

    def add(self, person: Person):
        self.room.append(person)

    def is_empty(self):
        return len(self.room) == 0

    def shortest(self):
        if self.is_empty():
            return None
        shortest_person = min(self.room, key=lambda p: p.height)
        return shortest_person.name

    def remove_shortest(self):
        if self.is_empty():
            return None
        shortest_person = min(self.room, key=lambda p: p.height)
        self.room.remove(shortest_person)
        return shortest_person

    def print_contents(self):
        total_count = len(self.room)
        total_height = sum(person.height for person in self.room)

        print(f'There are {total_count} persons in the room, and their combined height is {total_height} cm')
        for person in self.room:
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
