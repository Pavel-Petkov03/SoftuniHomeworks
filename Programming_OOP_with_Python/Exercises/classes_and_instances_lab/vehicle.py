class Vehicle:
    max_speed = 150
    def __init__(self, mileage):
        self.mileage = mileage
        self.gadgets = []
car = Vehicle(20)
print(car.max_speed)
print(car.mileage)
print(car.gadgets)
car.gadgets.append('Hudly Wireless')
print(car.gadgets)
