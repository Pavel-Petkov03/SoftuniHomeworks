class Pokemon:
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def pokemon_details(self):
        return f"{self.name} with health {self.health}"

