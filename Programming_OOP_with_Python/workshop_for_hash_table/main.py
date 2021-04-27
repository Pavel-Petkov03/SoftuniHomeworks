class HashTable:
    """
    This class is used to implement the logic of hash tables and dictionaries
    The moving index of simplicity is O1
    """

    def __init__(self):
        self.max_capacity = 4
        self.keys = [None] * self.max_capacity
        self.values = [None] * self.max_capacity

    def __getitem__(self, item):
        if item in self.keys:
            index = self.keys.index(item)
            return self.values[index]

    def __len__(self):
        return len(self.keys)

    def __setitem__(self, key, value):
        index = self.hash(key)
        self.__validate_collisions(index)
        self.keys[index] = key
        self.values[index] = value

    def __str__(self):
        return f'{[(self.keys[index] ,self.values[index]) for index in range(len(self.keys)) if self.keys[index]]}'

    def hash(self, key):
        index = sum([ord(char) for char in key]) % len(self.keys)
        validated_index = self.__validate_collisions(index)
        return validated_index

    def add(self, key, value):
        self[key] = value

    def get(self, key):
        index = self.keys.index(key)
        return self.values[index]

    def __resize_lists(self):
        if all(self.keys):
            self.keys = self.keys + [None] * self.max_capacity
            self.values = self.values + [None] * self.max_capacity
            self.max_capacity *= 2

    def __validate_collisions(self, index):
        if index == len(self.keys):
            self.__resize_lists()
            return self.__validate_collisions(0)
        if self.keys[index] is None:
            return index
        return self.__validate_collisions(index + 1)


table = HashTable()
table['name'] = 12
table['age'] = 12
table['value'] = 12
table['mmama'] = 12
table['tate'] = 12
print(table)
