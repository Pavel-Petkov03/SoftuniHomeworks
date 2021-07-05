class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.__budget -= price
            self.animals.append(animal)
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif len(self.animals) >= self.__animal_capacity:
            return "Not enough space for animal"
        return "Not enough budget"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        obj = self.find_worker_in_list_by_name(worker_name)
        if obj:
            self.workers.remove(obj[0])
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        sum_of_all_salaries = self.sum_all_salaries()
        if self.__budget >= sum_of_all_salaries:
            self.__budget -= sum_of_all_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        needed_money_to_tend = self.get_sum_of_all_tended()
        if self.__budget >= needed_money_to_tend:
            self.__budget -= needed_money_to_tend
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return 'You have no budget to tend the animals. They are unhappy.'

    def profit(self, price):
        self.__budget += price

    def animals_status(self):
        list_of_lions = self.find_list_by_type('Lion', self.animals)
        list_of_tigers = self.find_list_by_type('Tiger', self.animals)
        list_of_cheetahs = self.find_list_by_type('Cheetah', self.animals)
        result = [
            f'You have {len(self.animals)} animals',
            f'----- {len(list_of_lions)} Lions:',
            '\n'.join([str(l) for l in list_of_lions]),
            f'----- {len(list_of_tigers)} Tigers:',
            '\n'.join([str(l) for l in list_of_tigers]),
            f'----- {len(list_of_cheetahs)} Cheetahs:',
            '\n'.join([str(l) for l in list_of_cheetahs]),
        ]
        return '\n'.join(result)

    def workers_status(self):
        list_of_keepers = self.find_list_by_type('Keeper', self.workers)
        list_of_caretakers = self.find_list_by_type('Caretaker', self.workers)
        list_of_vets = self.find_list_by_type('Vet', self.workers)
        result = [
            f'You have {len(self.workers)} workers',
            f'----- {len(list_of_keepers)} Keepers:',
            '\n'.join([str(l) for l in list_of_keepers]),
            f'----- {len(list_of_keepers)} Caretakers:',
            '\n'.join([str(l) for l in list_of_caretakers]),
            f'----- {len(list_of_vets)} Vets:',
            '\n'.join([str(l) for l in list_of_vets]),
        ]
        return '\n'.join(result)

    # helper
    def find_worker_in_list_by_name(self, worker_name):
        return [w for w in self.workers if w.name == worker_name]

    def sum_all_salaries(self):
        return sum([w.salary for w in self.workers])

    def get_sum_of_all_tended(self):
        return sum([a.get_needs() for a in self.animals])

    @staticmethod
    def find_list_by_type(type_of_animal, list_of_types):
        return [a for a in list_of_types if a.__class__.__name__ == type_of_animal]
