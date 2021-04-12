from person.project import Animal
from person.project import Dog


class Teacher(Animal, Dog):
    @staticmethod
    def teach():
        return "teaching..."
