
class Player:
    def __init__(self, name, sprint, dribble, passing, shooting):
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    def __str__(self):
        return f'Player: {self.__name}\nSprint: {self.__sprint}\nDribble: {self.__dribble}\n' \
               f'Passing: {self.__passing}\nShooting: {self.__shooting}\n'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new):
        self.__name = new

    @property
    def sprint(self):
        return self.__sprint

    @sprint.setter
    def sprint(self, new):
        self.__sprint = new

    @property
    def dribble(self):
        return self.__dribble

    @dribble.setter
    def dribble(self, new):
        self.__dribble = new

    @property
    def passing(self):
        return self.__passing

    @passing.setter
    def passing(self, new):
        self.__passing = new

    @property
    def shooting(self):
        return self.__shooting

    @shooting.setter
    def shooting(self, new):
        self.__shooting = new



