
class Zoo:
    def __init__(self, name, budget, animals_capacity, workers_capacity):
        self.__animals_capacity = animals_capacity
        self.__workers_capacity = workers_capacity
        self.__budget = budget
        self.name = name
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) < self.__animals_capacity and self.__budget >= price:
            self.__budget -= price
            self.animals.append(animal)
            return f"{self.name} the {animal.NAME_OF_KIND} added to the zoo"
        elif self.__budget < price:
            return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{self.name} the {worker.NAME_OF_KIND} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        result = [obj for obj in self.workers if obj.name == worker_name]
        if result:
            worker_obj = result[0]
            self.workers.remove(worker_obj)
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        if self.__budget >= sum([obj.salary for obj in self.workers]):
            self.__budget -= sum([obj.salary for obj in self.workers])
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        if self.__budget >= sum([obj.get_needs() for obj in self.animals]):
            self.__budget -= sum([obj.get_needs() for obj in self.animals])
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self,amount):
        self.__budget += amount

    def animals_status(self):
        result = f'You have {len(self.animals)} animals\n'
        filters_lions = [lion for lion in self.animals if lion.NAME_OF_KIND == 'Lion']
        filtered_cheetahs = [cheetah for cheetah in self.animals if cheetah.NAME_OF_KIND == 'Cheetah']
        filtered_tigers = [tiger for tiger in self.animals if tiger.NAME_OF_KIND == 'Tiger']
        result += f'----- {len(filters_lions)} Lions:\n'
        for lion in filters_lions:
            result += str(lion)



