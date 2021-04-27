class Cheetah:
    NEEDED_MONEY_FOR_Cheetah = 60
    NAME_OF_KIND = 'Cheetah'

    def __init__(self, name, gender, age):
        self.name = name
        self.age = age
        self.gender = gender

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

    def get_needs(self):
        return Cheetah.NEEDED_MONEY_FOR_Cheetah

