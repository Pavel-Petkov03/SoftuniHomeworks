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

    def heal(self, survivor: Survivor, medicine_type: str):
        if survivor.needs_healing:
            for m in range(len(self.medicine) - 1, -1, -1):
                current_medicine = self.medicine[m]
                if medicine_type == current_medicine.__name__:
                    current_medicine.apply(survivor)
                    if survivor.health > 100:
                        survivor.health = 100
                    self.medicine.pop(m)
                    return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor: Survivor, sustenance_type: str):
        if survivor.needs_sustenance:
            for s in range(len(self.supplies) - 1, -1, -1):
                current_supply = self.supplies[s]
                if current_supply.__name__ == sustenance_type:
                    current_supply.apply(survivor)
                    if survivor.needs > 100:
                        survivor.needs = 100
                    self.supplies.pop(s)
                    return f"{survivor.name} sustained successfully with {sustenance_type}"

    def pop_food_and_water(self):
        result = []
        for value in reversed(self.water):
            result.append(self.supplies.remove(value))
        for value in reversed(self.food):
            result.append(self.supplies.remove(value))

        return result

    def next_day(self):
        for sur in self.survivors:
            sur.needs -= 2 * sur.age
            self.sustain(sur, self.pop_food_and_water()[0].__name__)
            self.sustain(sur, self.pop_food_and_water()[1].__name__)

