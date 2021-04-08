class Tiger:
    NEEDED_MONEY_FOR_Tiger = 45
    NAME_OF_KIND = 'Tiger'

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

    def get_needs(self):
        return Tiger.NEEDED_MONEY_FOR_Tiger

