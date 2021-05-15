from project.software.software import Software


class Hardware:
    def __init__(self, name, type_, capacity, memory):
        self.name = name
        self.type = type_
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software: Software):
        if not self.__validate_installation(software):
            raise Exception("Software cannot be installed")
        self.software_components.append(software)

    def uninstall(self, software:Software):
        if software in self.software_components:
            self.software_components.remove(software)

    @property
    def available_capacity(self):
        return self.capacity - sum([s.capacity_consumption for s in self.software_components])

    @property
    def available_memory(self):
        return self.memory - sum([s.memory_consumption for s in self.software_components])

    @property
    def total_used_capacity(self):
        return sum([s.capacity_consumption for s in self.software_components])

    @property
    def total_used_memory(self):
        return sum([s.memory_consumption for s in self.software_components])


    def __validate_installation(self, software):
        return self.available_capacity >= software.capacity_consumption and self.available_memory >= software.memory_consumption
