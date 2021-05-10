from abc import ABC


class Medicine(ABC):
    def __init__(self, h):
        self.__health_increase = h
        self.validate()

    def validate(self):
        if self.__health_increase < 0:
            raise ValueError("Health increase cannot be less than zero.")

    def apply(self, survivor):
        survivor.health += self.__health_increase
