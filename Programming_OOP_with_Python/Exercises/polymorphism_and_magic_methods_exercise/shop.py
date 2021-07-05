class Shop:
    def __init__(self, name, type_, capacity):
        self.name = name
        self.type = type_
        self.capacity = capacity
        self.items = {}
        self.counter = 0

    @classmethod
    def small_shop(cls, name, type_):
        return cls(name, type_, capacity=10)

    def add_item(self, item_name):
        if item_name not in self.items:
            self.items[item_name] = 0
        if self.counter == len(self.items):
            return "Not enough capacity in the shop"
        self.items[item_name] += 1
        self.counter += 1
        return f"{item_name} added to the shop"

    def remove_item(self, item_name, amount):
        if item_name in self.items and amount <= self.items[item_name]:
            self.items[item_name] -= amount
            self.counter -= amount
            return F"{amount} {item_name} removed from the shop"
        return  f"Cannot remove {amount} {item_name}"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
print(fresh_shop)
print(small_shop)

print(fresh_shop.add_item("Bananas"))
print(fresh_shop.remove_item("Tomatoes", 2))

print(small_shop.add_item("Jeans"))
print(small_shop.add_item("Jeans"))
print(small_shop.remove_item("Jeans", 2))
