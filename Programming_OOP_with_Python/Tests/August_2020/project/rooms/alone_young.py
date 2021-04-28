from project.rooms.room import Room
from project.appliances.tv import TV


class AloneYoung(Room):
    room_cost = 10
    appliances = [TV()]

    def __init__(self, family_name, salary):
        super().__init__(family_name, salary, 1)
