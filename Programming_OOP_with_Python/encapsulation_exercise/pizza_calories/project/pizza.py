


class Pizza:
    def __init__(self, name, dough, toppings_capacity):
        self.__name = name
        self.__dough = dough
        self.__toppings_capacity = toppings_capacity
        self.__toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_value):
        self.__name = new_value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, new_value):
        self.__dough = new_value

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, new_value):
        self.__toppings_capacity = new_value

    def add_topping(self, topping):
        if self.__toppings_capacity == len(self.__toppings):
            raise ValueError('Not enough space for another topping')
        elif topping.topping_type in self.__toppings:
            self.__toppings[topping.topping_type] += topping.weight
        else:
            self.__toppings[topping.topping_type] = topping.weight

    def calculate_total_weight(self):
        return sum([weight for type_, weight in self.__toppings.items()])


