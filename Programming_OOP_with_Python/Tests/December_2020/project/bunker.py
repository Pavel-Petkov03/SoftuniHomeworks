from project.supply.food_supply import FoodSupply
from project.supply.water_supply import WaterSupply
from project.medicine.painkiller import Painkiller
from project.medicine.salve import Salve
from project.survivor import Survivor


class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        result = [f for f in self.supplies if isinstance(f, FoodSupply)]
        if len(result) == 0:
            raise IndexError("There are no food supplies left!")
        return result

    @property
    def water(self):
        result = [w for w in self.supplies if isinstance(w, WaterSupply)]
        if len(result) == 0:
            raise IndexError("There are no water supplies left!")

        return result

    @property
    def painkillers(self):
        result = [p for p in self.medicine if isinstance(p, Painkiller)]
        if len(result) == 0:
            raise IndexError("There are no painkillers left!")
        return result

    @property
    def salves(self):
        result = [p for p in self.medicine if isinstance(p, Salve)]
        if len(result) == 0:
            raise IndexError("There are no salves left!")
        return result

    def add_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type: str):
        if survivor.needs_healing:
            result = None
            if medicine_type == 'Painkiller':
                result = self.painkillers[-1]
            elif medicine_type == 'Salve':
                result = self.salves[-1]
            self.medicine.remove(result)
            result.apply(survivor)
            if survivor.health > 100:
                survivor.health = 100
            return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor: Survivor, substance_type: str):
        if survivor.needs_sustenance:
            result = None
            if substance_type == 'WaterSupply':
                result = self.water[-1]
            elif substance_type == 'FoodSupply':
                result = self.food[-1]
            self.supplies.remove(result)
            result.apply(survivor)
            if survivor.needs > 100:
                survivor.needs = 100
            return f"{survivor.name} sustained successfully with {substance_type}"

    def next_day(self):
        for sur in self.survivors:
            sur.needs -= sur.age * 2
            self.sustain(sur, 'WaterSupply')
            self.sustain(sur, 'FoodSupply')


