from project.medicine.medicine import Medicine


class Salve(Medicine):
    def __init__(self):
        super().__init__(50)
        self.__health_increase = 50

