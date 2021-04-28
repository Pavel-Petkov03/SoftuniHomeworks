from project.rooms.room import Room
from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV


class OldCouple(Room):
    room_cost = 15
    appliances = [TV(), Fridge(), Stove()]

    def __init__(self, family_name, pension_one, pension_two):
        super().__init__(family_name, pension_one + pension_two,2)


