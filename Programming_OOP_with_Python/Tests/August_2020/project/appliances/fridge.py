from project.appliances.appliance import Appliance


class Fridge(Appliance):
    def __init__(self):
        super(Fridge, self).__init__(1.2)

