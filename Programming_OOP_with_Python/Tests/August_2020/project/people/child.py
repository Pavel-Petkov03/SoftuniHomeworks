class Child:
    def __init__(self, food_cost, *toys_cost):
        self.cost = food_cost + sum(toys_cost)

