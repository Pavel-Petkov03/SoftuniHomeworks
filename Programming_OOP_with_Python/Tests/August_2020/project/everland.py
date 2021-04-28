class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        return f"Monthly consumption: {self.final_result_for_monthly_consumption_of_all_rooms()}$."

    def final_result_for_monthly_consumption_of_all_rooms(self):
        result = 0
        for room in self.rooms:
            result += sum([fur.get_monthly_expense() for fur in room.appliance])
            if hasattr(room, 'children'):
                result += sum([child.cost * 30 for child in room.children])
        return result

    @staticmethod
    def final_consumption_for_one_room_per_month(room):
        result = []
        result += sum([fur.get_monthly_expense() for fur in room.appliance])
        if hasattr(room, 'children'):
            result += sum([child.cost * 30 for child in room.children])

        return result

    def pay(self):
        final = []
        for room in self.rooms:
            consumption = self.final_consumption_for_one_room_per_month(room)
            if room.budget >= consumption:
                final.append(
                    f"{room.family_name} paid {consumption:.2f}$ and have {(room.budget - consumption):.2f}$ left.")
                room.budget -= consumption
            else:
                final.append(f'{room.family_name} does not have enough budget and must leave the hotel.')
                self.rooms.remove(room)

        return "\n".join(final)

    def check_all_people_in_the_hotel(self):
        result = 0
        for room in self.rooms:
            result += room.members_count

        return result

    def status(self):
        result = []
        result.append(f"Total population: {self.check_all_people_in_the_hotel()}")


