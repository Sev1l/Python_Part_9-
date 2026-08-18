## Objects as attributes
# Task 2 (A box of presents)


class Present:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f'{self.name} ({self.weight} kg)'


class Box:
    def __init__(self):
        self.box_list = []
        self.total = 0

    def add_present(self, present: Present):
        self.box_list.append(present)
        self.total += present.weight

    def total_weight(self):
        return self.total


book = Present("ABC Book", 2)
print("The name of the present:", book.name)
print("The weight of the present:", book.weight)
print("Present:", book)
box = Box()
box.add_present(book)
print(box.total_weight())
cd = Present("Pink Floyd: Dark Side of the Moon", 1)
box.add_present(cd)
print(box.total_weight())
