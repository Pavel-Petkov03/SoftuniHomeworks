from abc import ABC, abstractmethod


class Medicine(ABC):
    @abstractmethod
    def __init__(self, h):
        self.health_increase = h

    @property
    def health_increase(self):
        return self.__health_increase

    @health_increase.setter
    def health_increase(self, value):
        if value < 0:
            raise ValueError("Health increase cannot be less than zero.")
        self.__health_increase = value

    def apply(self, survivor):
        survivor.health += self.health_increase
