class Topping:
    def __init__(self, topping_type, weight):
        self.topping_type = topping_type
        self.weight = weight

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, new_value):
        if new_value <= 0:
            raise ValueError("The weight cannot be less or equal to zero")
        self.__weight = new_value

    @property
    def topping_type(self):
        return self.__topping_type

    @topping_type.setter
    def topping_type(self, new_value):
        if new_value == '':
            raise ValueError("The topping type cannot be an empty string")
        self.__topping_type = new_value
