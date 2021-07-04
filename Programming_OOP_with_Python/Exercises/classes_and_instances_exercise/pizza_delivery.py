class PizzaDelivery:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient, quantity, ingredient_price):
        if self.ordered:
            return self.make_order()
        if ingredient not in self.ingredients:
            self.ingredients[ingredient] = 0
        self.ingredients[ingredient] += quantity
        self.price += ingredient_price * quantity

    def remove_ingredient(self, ingredient: str, quantity: int, ingredient_price: float):
        if self.ordered:
            return self.make_order()
        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        elif self.ingredients[ingredient] < quantity:
            return f"Please check again the desired quantity of {ingredient}!"
        self.ingredients[ingredient] -= quantity
        self.price -= ingredient_price * quantity

    def make_order(self):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        self.ordered = True
        return f"You've ordered pizza {self.name} prepared with {', '.join([f'{key}: {value}' for key, value in self.ingredients.items()])} and the price will be {self.price}lv."


# margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
# margarita.add_extra('mozzarella', 1, 0.5)
# margarita.add_extra('cheese', 1, 1)
# margarita.remove_ingredient('cheese', 1, 1)
# print(margarita.remove_ingredient('bacon', 1, 2.5))
# print(margarita.remove_ingredient('tomatoes', 2, 0.5))
# margarita.remove_ingredient('cheese', 2, 1)
# print(margarita.make_order())
# print(margarita.add_extra('cheese', 1, 1))


import unittest


import unittest


class Tests(unittest.TestCase):
    def test_init(self):
        t = PizzaDelivery('Margarita', 12, {'cheese': 2, 'tomatoes': 1})
        self.assertEqual(t.name, 'Margarita')
        self.assertEqual(t.price, 12)
        self.assertEqual(t.ingredients, {'cheese': 2, 'tomatoes': 1})
        self.assertEqual(t.ordered, False)

    def test_add_extra_with_available_ingredient_should_increase_the_quantity(self):
        t = PizzaDelivery('Margarita', 12, {'cheese': 2, 'tomatoes': 1})
        t.add_extra('cheese', 1, 2)
        self.assertEqual(t.ingredients, {'cheese': 3, 'tomatoes': 1})
        self.assertEqual(t.price, 14)

    def test_add_extra_with_new_ingredient_should_add_the_quantity(self):
        t = PizzaDelivery('Margarita', 12, {'cheese': 2, 'tomatoes': 1})
        t.add_extra('mozzarella', 1, 2.5)
        self.assertEqual(t.ingredients, {'cheese': 2, 'tomatoes': 1, 'mozzarella': 1})
        self.assertEqual(t.price, 14.5)

    def test_remove_ingredients_not_included_in_pizza_should_return_message(self):
        t = PizzaDelivery('Margarita', 12, {'cheese': 2, 'tomatoes': 1})
        message = t.remove_ingredient('bacon', 1, 5)
        self.assertEqual(t.ingredients, {'cheese': 2, 'tomatoes': 1})
        self.assertEqual(message, 'Wrong ingredient selected! We do not use bacon in Margarita!')

    def test_remove_ingredients_with_quantity_higher_than_what_we_have_should_return_message(self):
        t = PizzaDelivery('Margarita', 12, {'cheese': 2, 'tomatoes': 1})
        message = t.remove_ingredient('tomatoes', 2, 2)
        self.assertEqual(t.ingredients, {'cheese': 2, 'tomatoes': 1})
        self.assertEqual(message, 'Please check again the desired quantity of tomatoes!')

    def test_remove_ingredients_with_quantity_equal_to_what_we_have_should_remove_the_ingredient(self):
        t = PizzaDelivery('Margarita', 12, {'cheese': 2, 'tomatoes': 1})
        t.remove_ingredient('tomatoes', 1, 2)
        self.assertEqual(t.ingredients, {'cheese': 2, 'tomatoes': 0})
        self.assertEqual(t.price, 10)

    def test_pizza_ordered(self):
        t = PizzaDelivery('Margarita', 12, {'cheese': 2, 'tomatoes': 1})
        result = t.make_order()
        self.assertEqual(t.ordered, True)
        self.assertEqual(result,
                         "You've ordered pizza Margarita prepared with cheese: 2, tomatoes: 1 and the price will be 12lv.")

    def test_add_extra_after_pizza_is_ordered_should_return_message(self):
        t = PizzaDelivery('Margarita', 12, {'cheese': 2, 'tomatoes': 1})
        order = t.make_order()
        result = t.add_extra('mozzarella', 1, 2)
        self.assertEqual(order,
                         "You've ordered pizza Margarita prepared with cheese: 2, tomatoes: 1 and the price will be 12lv.")
        self.assertEqual(result, "Pizza Margarita already prepared, and we can't make any changes!")

    def test_remove_ingredient_after_pizza_is_ordered_should_return_message(self):
        t = PizzaDelivery('Margarita', 12, {'cheese': 2, 'tomatoes': 1})
        order = t.make_order()
        result = t.remove_ingredient('mozzarella', 1, 2)
        self.assertEqual(order,
                         "You've ordered pizza Margarita prepared with cheese: 2, tomatoes: 1 and the price will be 12lv.")
        self.assertEqual(result, "Pizza Margarita already prepared, and we can't make any changes!")


if __name__ == "__main__":
    unittest.main()