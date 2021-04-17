class Robot:
    def __init__(self, name):
        self.name = name

    def get_type(self):
        return self.name


class Android(Robot):

    @staticmethod
    def senzors_count():
        return 4


class Chappie(Robot):

    @staticmethod
    def senzors_count():
        return 6


robots = [Android('Robocop'), Chappie('XIX')]
for r in robots:
    print(r.senzors_count())
