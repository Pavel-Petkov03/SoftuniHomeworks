
class Software:
    def __init__(self, name , type_ , capacity_consumption, memory_consumption):
        self.name = name
        self.type = type_
        self.capacity_consumption = capacity_consumption
        self.memory_consumption = memory_consumption

    def __repr__(self):
        return f'{self.name}'




