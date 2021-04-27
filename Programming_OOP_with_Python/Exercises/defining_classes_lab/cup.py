# Create a class called Book. It should have an __init__() method that should receive:
# •	name : string
# •	author : string
# •	pages : int
# Submit only the class in the judge system.


class Cup:
    def __init__(self,size,quantity):
        self.quantity = quantity
        self.size = size

    def fill(self,fill):
        if self.quantity + fill <= self.size:
            self.quantity += fill

    def status(self):
        return self.size - self.quantity

cup = Cup(100, 50)
cup.fill(20)
cup.fill(10)
print(cup.status())


