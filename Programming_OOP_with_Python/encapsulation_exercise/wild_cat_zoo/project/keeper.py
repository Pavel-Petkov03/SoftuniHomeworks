class Keeper:
    NAME_OF_KIND = 'Keeper'
    def __init__(self, name, age, salary):
        self.age = age
        self.salary = salary
        self.name = name

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"
