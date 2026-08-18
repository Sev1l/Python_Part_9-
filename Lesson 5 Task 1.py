## Class attributes
# Task 1 (List Helper)


from collections import Counter


class ListHelper:
    @staticmethod
    def greatest_frequency(my_list: list):
        counts = Counter(my_list)
        return counts.most_common(1)[0][0]

    @staticmethod
    def doubles(my_list: list):
        counts = Counter(my_list)
        for item, count in counts.items():
            if count == 2:
                return item


numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
print(ListHelper.greatest_frequency(numbers))
print(ListHelper.doubles(numbers))

