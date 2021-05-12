class Child:
    def __init__(self, food_cost, *toys):
        self.cost = food_cost + sum(toys)

    def get_monthly_expense(self):
        return self.cost * 30




