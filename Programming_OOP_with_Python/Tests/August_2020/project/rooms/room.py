class Room:
    def __init__(self, family_name, budget, members_count):
        self.room_cost = 0
        self.children = []
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.expenses = 0

    @staticmethod
    def generate_appliances(members, *args):
        result = []
        for _ in range(members):
            for appliance in args:
                result.append(appliance())
        return result

    @property
    def total_sum(self):
        return self.expenses + self.room_cost

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        result = 0
        for arg in args:
            result += sum([a.get_monthly_expense() for a in arg])
        self.expenses = result
