class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        return f"Monthly consumption: {sum(room.total_sum for room in self.rooms):.2f}$."

    def pay(self):
        result = []
        for room in self.rooms:
            room_final_cost = room.total_sum
            if room.budget >= room_final_cost:
                result.append(f"{room.family_name} paid {room_final_cost:.2f}$ and have {room.budget:.2f}$ left.")
                room.budget -= room_final_cost
            else:
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.remove(room)

        return "\n".join(result)

    def count_all_people(self):
        return sum(room.members_count for room in self.rooms)

    def status(self):
        result = [f'Total population: {self.count_all_people()}']
        for room in self.rooms:
            result.append(
                f'{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$'
            )
            n = 1
            for child in room.children:
                result.append(f"--- Child {n} monthly cost: {(child.get_monthly_expense()):.2f}$")
                n += 1
            monthly_appliance = sum(ap.get_monthly_expense() for ap in room.appliances)
            result.append(f'--- Appliances monthly cost: {monthly_appliance:.2f}$')
        return "\n".join(result)

