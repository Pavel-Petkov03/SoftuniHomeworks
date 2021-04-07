class ExercisePlan:
    id_ = 0

    def __init__(self, trainer_id, equipment_id, duration):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = self.get_next_id()

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):
        return cls(trainer_id, equipment_id, hours)

    @staticmethod
    def get_next_id():
        ExercisePlan.id_ += 1
        return ExercisePlan.id_

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"
