from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_consumption = fuel_consumption
        self.fuel_quantity = fuel_quantity

    def drive(self, distance):
        self.fuel_consumption += 0.9
        if self.fuel_quantity >= self.fuel_consumption * distance:
            self.fuel_quantity -= self.fuel_consumption * distance

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_consumption = fuel_consumption
        self.fuel_quantity = fuel_quantity

    def drive(self, distance):
        self.fuel_consumption += 1.6
        if self.fuel_quantity >= self.fuel_consumption * distance:
            self.fuel_quantity -= self.fuel_consumption * distance


    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)

