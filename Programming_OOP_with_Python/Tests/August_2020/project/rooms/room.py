class Room:
    def __init__(self, name, budget, members_count):
        self.name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.__expenses = None

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if self.__expenses < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        for element in args:
            self.expenses += [somebody.cost() for somebody in element]
