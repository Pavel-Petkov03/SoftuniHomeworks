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
            self.rooms[actual_index].take_room(people)

    def free_room(self, room_number):
        find = self.find_room(room_number, self.rooms)
        if find:
            actual_index = find[0]
            self.rooms[actual_index].free_room()

    def status(self):
        result = ''
        free = ", ".join([str(room.number) for room in self.rooms if not room.is_taken])
        taken = ", ".join([str(room.number) for room in self.rooms if room.is_taken])
        result += f'Hotel {self.name} has {self.guests} total guests\n'
        result += f'Free rooms: {free}\n'
        result += f'Taken rooms: {taken}'
        return result

    @property
    def guests(self):
        return sum([r.guests for r in self.rooms])

    @guests.setter
    def guests(self, value):
        self.__guests = value

