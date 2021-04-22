class IntegerList:
    def __init__(self, list_of_ints):
        self.list_of_ints = list_of_ints

    @staticmethod
    def __validate_index(index, list_of_int):
        return 0 <= index < len(list_of_int)

    @staticmethod
    def __validate_type(t):
        return isinstance(int, type(t))

    def add(self, el):
        if self.__validate_type(el):
            self.list_of_ints.append(el)
            return self.list_of_ints
        raise ValueError()

    def remove_index(self, index):
        if self.__validate_index(index, self.list_of_ints):
            return self.list_of_ints.pop(index)
        raise IndexError()

    def get(self, index):
        if self.__validate_index(index, self.list_of_ints):
            return self.list_of_ints[index]
        raise IndexError()

    def insert(self, index, element):
        if self.__validate_type(element):
            raise ValueError()
        elif self.__validate_index(index, self.list_of_ints):
            raise IndexError()

        self.list_of_ints.insert(index, element)

    def get_biggest(self):
        return max(self.list_of_ints)

    def get_index(self, element):
        if element in self.list_of_ints:
            return self.list_of_ints.index(element)




import unittest

class MyTests(unittest.TestCase):
    def test_for(self):
        pass

