from project.rooms.room import Room
from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV


class YoungCoupleWithChildren(Room):
    room_cost = 30
    appliances = [TV(), Fridge(), Laptop()]

    def __init__(self, family_name, salary_one, salary_two, *children):
        super().__init__(family_name, salary_one + salary_two, 2 + len(children))
        self.children = list(children)



