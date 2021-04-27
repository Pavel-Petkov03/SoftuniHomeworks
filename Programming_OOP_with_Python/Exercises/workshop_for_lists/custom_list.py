

class RefactorNoneListToNormal:
    def choose(self, index, array):
        if index == 0:
            return 1
        elif index == len(array) - 1:
            return -2
        elif 0 < index < len(array):
            return index


class CustomList(RefactorNoneListToNormal):
    """
    This is new implementation for list in which every time when you add a value dynamically adds None behind
    and opposite the list
    """

    def __init__(self, my_list=[]):
        self.list = [None] + my_list + [None]

    def append(self, new_value):
        self.list[-1] = new_value
        self.list = self.list + [None]
        return self.__filter_from_none_values()
        # making always the last value None in order not to find index error

    def remove(self, index):
        if self.__validate_index(index):
            raise IndexError('Index not in range')
        removal_index = self.choose(index, self.list)
        returned_value = self.list[removal_index]
        self.list[removal_index] = None
        return returned_value

    def get(self, index):
        if self.__filter_from_none_values()[index] is None:
            raise IndexError('Index not in range')
        wanted_index = self.choose(index, self.list)
        return self.list[wanted_index]

    def extend(self, iterable):
        self.__validate_if_iterable_object(iterable)
        for ex in iterable:
            self.list[-1] = ex
            self.list += [None]
        return self.__filter_from_none_values()

    def insert(self, index, value):
        if index == 0:
            self.list = [None] + [value] + self.list
        elif index < len(self.list):
            self.list = self.list[:index] + [value] + self.list[index:]
        else:
            self.list = self.list + [value] + [None]
        return self.__filter_from_none_values()

    def pop(self):
        value = self.list[-2]  # because our last value will always be None
        self.list[-2] = None
        self.list = self.list[:-1]
        return value

    @classmethod
    def clear(cls):
        return cls([])

    def index(self, value):
        for i in self.__filter_from_none_values():
            if i == value:
                return i

    def count(self, value):
        return len([count for count in self.__filter_from_none_values() if count == value])

    def reverse(self):
        return self.__filter_from_none_values().__reversed__()

    def copy(self):
        return CustomList(self.__filter_from_none_values())

    def size(self):
        return len(self.__filter_from_none_values())

    def add_first(self, value):
        self.list = [None] + [value] + self.list[1:]  # make implementation like deque

    def dictionize(self):
        dect = {}
        my_list = self.__filter_from_none_values()
        for index in range(0, len(my_list), 2):
            if index + 1 not in range(len(my_list)):
                dect = {my_list[index]: " "}
            else:
                dect = {my_list[index]: my_list[index + 1]}

        return dect

    def move(self, amount):
        counter = 0
        index = 0
        while counter < amount:
            if self.list[index] is not None:
                value = self.list[index]
                counter += 1
                self.list[index] = None
                self.list = self.list[1:]
                self.append(value)
            if index == len(self.list):
                raise Exception('Not enough values to move')
            index += 1

    def sum(self):
        final_sum = 0
        for value in self.__filter_from_none_values():
            final_sum += value if type(value) in [int, str] else len(value)
        return final_sum

    def overbound(self):
        return max(self.__main_board_logic(), key=lambda x: x[1])[0]

    def underbound(self):
        return min(self.__main_board_logic(), key=lambda x: x[1])[0]

    def __main_board_logic(self):
        ls = self.__filter_from_none_values()
        return [(index, ls[index]) if ls[index] in [float , index] else (index, len(ls[index]))for index in
                range(len(ls))]

    def __validate_index(self, index):
        return index > len(self.__filter_from_none_values())

    def __filter_from_none_values(self):
        return [f for f in self.list if f is not None]

    @staticmethod
    def __validate_if_iterable_object(iterable):
        try:
            iter(iterable)
        except TypeError:
            raise TypeError('This object is not iterable')


cus = CustomList([1, 2, 3])
cus.insert(7, 12)
cus.add_first(1)
print(cus.list)
print(cus.sum())
print(cus.extend([1]))
b = cus.copy()
