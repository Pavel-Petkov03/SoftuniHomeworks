
class FreePerson:

    def __init__(self, position):
        self.position = position

    def walk_north(self, dist):
        self.position[1] += dist

    def walk_east(self, dist):
        self.position[0] += dist


class Prisoner:
    PRISON_LOCATION = (3, 3)

    def __init__(self):
        self.is_free = False

    @property
    def position(self):
        return Prisoner.PRISON_LOCATION



prisoner = Prisoner()
print("The prisoner trying to walk to north by 10 and east by -3")
try:
    prisoner.walk_north(10)
    prisoner.walk_east(-3)
except:
    pass

print(f"The location of the prison:{prisoner.PRISON_LOCATION}")
print("The current position of the")
print(f"prisoner: {prisoner.position}")

