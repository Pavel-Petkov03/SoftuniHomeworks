class Store:
    def __init__(self, name: str, type_: str, capacity: int):
        self.name = name
        self.type = type_
        self.capacity = capacity
        self.items = {}

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"

    @classmethod
    def from_size(cls, name, type_, size):
        return cls(name, type_, size / 2)

    @staticmethod
    def check_for_max_capacity(store_dict, capacity):
        return sum([k for k in store_dict.values()]) > capacity

    def add_item(self, item_name: str):
        if self.check_for_max_capacity(self.items, self.capacity):
            return "Not enough capacity in the store"
        if item_name not in self.items:
            self.items[item_name] = 0
        self.items[item_name] += 1
        return f"{item_name} added to the store"

    def remove_item(self, item_name: str, amount: int):
        if item_name in self.items and self.items[item_name] >= amount:
            self.items[item_name] -= amount
            return f"{amount} {item_name} removed from the store"
        return f"Cannot remove {amount} {item_name}"



