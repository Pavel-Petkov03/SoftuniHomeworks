class Trainer:
    id_ = 1

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Trainer <{Trainer.id_}> {self.name}"

    @staticmethod
    def get_next_id():
        return Trainer.id_ + 1




