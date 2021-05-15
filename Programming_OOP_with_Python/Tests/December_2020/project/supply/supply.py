
class Supply:
    def __init__(self, i):
        self.needs_increase = i
        self.validate()

    def validate(self):
        if self.needs_increase < 0:
            raise ValueError("Needs increase cannot be less than zero.")

    def apply(self, survivor):
        survivor.needs += self.needs_increase


