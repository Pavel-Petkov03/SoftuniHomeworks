


class Dough:
    def __init__(self, flour_type, baking_technique, weight):
        self.flour_type = flour_type
        self.baking_technique = baking_technique
        self.weight = weight

    @property
    def flour_type(self):
        return self.__flour_type

    @property
    def baking_technique(self):
        return self.__baking_technique

    @property
    def weight(self):
        return self.__weight

    @flour_type.setter
    def flour_type(self, new_type):
        if new_type == "":
            raise ValueError("The flour type cannot be an empty string")
        self.__flour_type = new_type

    @baking_technique.setter
    def baking_technique(self, new_type):
        if new_type == "":
            raise ValueError("The baking technique cannot be an empty string")
        self.__baking_technique = new_type

    @weight.setter
    def weight(self, new_type):
        if new_type <= 0:
            raise ValueError("The weight cannot be less or equal to zero")
        self.__weight = new_type
