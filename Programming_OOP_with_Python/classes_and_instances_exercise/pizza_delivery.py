class PizzaDelivery:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.ingredients = ingredients
        self.price = price
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, ingredient_price: float):
        if self.ordered:
            return self.make_order()
        if ingredient not in self.ingredients:
            self.ingredients[ingredient] = quantity
            self.price += quantity * ingredient_price
        else:
            self.ingredients[ingredient] += quantity
            self.price += quantity * ingredient_price

    def remove_ingredient(self, ingredient: str, quantity: int, ingredient_price: float):
        if ingredient in self.ingredients:
            if quantity > self.ingredients[ingredient]:
                return f"Please check again the desired quantity of {ingredient}!"
            self.ingredients[ingredient] -= quantity
            self.price -= quantity * ingredient_price
        if self.ordered:
            return self.make_order()
        else:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"

    def make_order(self):
        if self.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"
        self.ordered = True
        return f"You've ordered pizza {self.name} prepared with {', '.join([f'{key}: {value}' for key, value in self.ingredients.items()])} and the price will be {self.price}lv."





