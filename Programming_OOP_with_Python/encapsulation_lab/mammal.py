class Mammal:
    __kingdom = 'animals'

    def __init__(self, name, type_, sound):
        self.type = type_
        self.sound = sound
        self.name = name

    def make_sound(self):
        return f"{self.name} makes {self.sound}"

    def get_kingdom(self):
        return Mammal.__kingdom

    def info(self):
        return f"{self.name} is of type {self.type}"



mammal = Mammal("Dog", "Domestic", "Bark")
print(mammal.make_sound())
print(mammal.get_kingdom())
print(mammal.info())
