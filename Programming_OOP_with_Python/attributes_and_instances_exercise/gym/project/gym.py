class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    @staticmethod
    def check_if_object_in_list(obj, list_with_objects):
        return obj not in list_with_objects

    @staticmethod
    def get_object_by_id(initial_id, list_of_objects):
        return [idi for idi in list_of_objects if idi.id_ == initial_id][0]

    def add_customer(self, customer):
        if self.check_if_object_in_list(customer, self.customers):
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if self.check_if_object_in_list(trainer, self.trainers):
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if self.check_if_object_in_list(equipment, self.equipment):
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if self.check_if_object_in_list(plan, self.plans):
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if self.check_if_object_in_list(subscription, self.subscriptions):
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        subscription_object = self.get_object_by_id(subscription_id, self.subscriptions)
        customer_object = self.get_object_by_id(subscription_object.customer_id, self.customers)
        trainer_object = self.get_object_by_id(subscription_object.trainer_id, self.trainers)
        equipment_object = self.get_object_by_id(subscription_object.exercise_id, self.equipment)

        return str(customer_object) + str(trainer_object) + str(equipment_object)
