class Room:
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    def take_room(self):
        if self.is_taken or self.guests + 1 <= self.capacity:
            return "Room number {number} cannot be taken"
        self.guests += 1

    def free_room(self):
        if self.is_taken:
            self.is_taken = False
            return
        return f"Room number {self.number} is not taken"
