from project.animal import Animal
from project.dog import Dog


class Teacher(Animal, Dog):
    @staticmethod
    def teach():
        return "teaching..."
