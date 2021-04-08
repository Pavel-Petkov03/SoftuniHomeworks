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
