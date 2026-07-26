## Class attributes
# Task 1 (List Helper)


class ListHelper:
    @staticmethod
    def greatest_frequency(my_list:list):
        counts = 0
        number = 0
        for i in my_list:
            if counts < my_list.count(i):
                counts = my_list.count(i)
                number = i
        return number
    @staticmethod
    def doubles(my_list:list):
        for i in my_list:
            if my_list.count(i) == 2:
                return i



numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
print(ListHelper.greatest_frequency(numbers))
print(ListHelper.doubles(numbers))
