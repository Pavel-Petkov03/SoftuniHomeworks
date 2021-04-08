class Lion:
    NEEDED_MONEY_FOR_LION = 50
    NAME_OF_KIND = 'Lion'

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

    def get_needs(self):
        return Lion.NEEDED_MONEY_FOR_LION
