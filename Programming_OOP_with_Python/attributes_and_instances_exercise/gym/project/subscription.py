class Subscription:
    id_ = 1

    def __init__(self, date, customer_id, trainer_id, exercise_id):
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id

    def __repr__(self):
        return f"Subscription <{Subscription.id_}> on {self.date}"

    @staticmethod
    def get_next_id():
        return Subscription.id_ + 1