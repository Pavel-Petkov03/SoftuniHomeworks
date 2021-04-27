"""
•	append(value) - Adds a value to the end of the list. Returns the list.
•	remove(index) - Removes the value on the index. Returns the value removed.
•	get(index) - Returns the value on the index.
•	extend(iterable) - Appends the iterable to the list. Returns the new list.
•	insert(index, value) - Adds the value on the specific index. Returns the list.
•	pop() - Removes the last value and returns it.
•	clear() - Removes all values, contained in the list.
•	index(value) - Returns the index of the given value.
•	count(value) - Returns the number of times the value is contained in the list.
•	reverse() - Returns the values of the list in reverse order.
•	copy() - Returns a copy of the list.

We will also add our own custom functionalities:
•	size() - Returns the length of the list.
•	add_first(value) - Adds the value at the beginning of the list
•	dictionize() - Returns the list as a dictionary: The keys will be each value on an even position and their values will be each value on an odd position. If the last value on an even position, it’s value will be " " (space)
•	move(amount) - Move the first "amount" of values to the end of the list. Returns the list.
•	sum() - Returns the sum of the list. If the value is not a number, add the length of the value to the overall number.
•	overbound() - Returns the index of the biggest value. If the value is not a number, check it’s length.
•	underbound() - Returns the index of the smallest value. If the value is not a number, check it’s length.

Do not inherit List. Feel free to implement your own functionality (and unit tests) or to write the methods by yourself.

"""


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
    I am making an implementation of list with index 0 will be
    """

    def __init__(self, my_list=[]):
        self.list = [None] + my_list + [None]

    def append(self, new_value):
        self.list[-1] = new_value
        self.list = self.list + [None]
        # making always the last value None in order not to find index error

    def remove(self, index):
        if self.__filter_from_none_values()[index] is None:
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
        self.__validate_index(iterable)
        for ex in self.list:
            self.list = self.list + [None]
            self.list[-1] = ex
        self.list = self.list + [None]
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
        return self.list.__reversed__()

    @classmethod
    def copy(cls):
        return cls()

    def size(self):
        return len([big for big in self.list if big is not None])

    def add_first(self, value):
        self.list = [None] + [value] + self.list[1:]

    def dictionize(self):
        pass

    def move(self, amount):
        pass

    def sum(self):
        final_sum = 0
        for value in self.list:
            if value is not None:
                final_sum += value if type(value) in [int, str] else len(value)
        return final_sum

    def overbound(self):
        pass

    def underbound(self):
        pass

    def __helper_resizing_func(self):
        pass

    def __validate_index(self, index):
        return self.list[index] is not None

    def __filter_from_none_values(self):
        return [f for f in self.list if f is not None]

    @staticmethod
    def __validate_if_iterable_object(iterable):
        try:
            iter(iterable)
        except TypeError:
            raise TypeError('This object is not iterable')
