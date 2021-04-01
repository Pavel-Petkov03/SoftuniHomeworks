class Store:
    def __init__(self, name: str, type_: str, capacity: int):
        self.name = name
        self.type = type_
        self.capacity = capacity
        self.store = {}

    def from_size(self, name, type_, size):
        self.__setattr__(name, type_(size))

    def add_item(self, item_name: str):
        if item_name in self.store:
            self.store[item_name] += 1
            return f"{item_name} added to the store"
        # TODO
        return "Not enough capacity in the store"

    def remove_item(self, item_name: str, amount: int):
        if item_name in self.store and self.store[item_name] >= amount:
            self.store[item_name] -= amount
            return f"{amount} {item_name} removed from the store"
        return f"Cannot remove {amount} {item_name}"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"
