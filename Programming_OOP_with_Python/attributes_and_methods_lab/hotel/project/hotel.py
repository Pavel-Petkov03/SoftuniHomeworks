from room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f'{stars_count} stars Hotel')

    @staticmethod
    def find_room(room_number, list_of_rooms):
        return [index for index in range(len(list_of_rooms)) if list_of_rooms[index].number == room_number]

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        find = self.find_room(room_number, self.rooms)
        if find:
            actual_index = find[0]
            if self.rooms[actual_index].guests + people <= self.rooms[actual_index].capacity:
                self.rooms[actual_index].guests += people
                self.guests += people
                self.rooms[actual_index].is_taken = True

    def free_room(self, room_number):
        find = self.find_room(room_number, self.rooms)
        if find:
            number = find[0]
            self.guests -= self.rooms[number].guests
            self.rooms[number].guests = 0
            self.rooms[number].is_taken = False

    def print_status(self):
        result = f'Hotel {self.name} has {self.guests} total guests\n'
        result += f'Free rooms: {", ".join([str(room.number) for room in self.rooms if not room.is_taken])}\n'
        result += f'Taken rooms: {", ".join([str(room.number) for room in self.rooms if room.is_taken])}'
        print(result)
