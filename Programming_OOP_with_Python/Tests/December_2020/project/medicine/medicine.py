
class Medicine:
    def __init__(self, h):
        self.health_increase = h
        self.validate()

    def validate(self):
        if self.health_increase < 0:
            raise ValueError("Health increase cannot be less than zero.")

    def apply(self, survivor):
        survivor.health += self.health_increase
