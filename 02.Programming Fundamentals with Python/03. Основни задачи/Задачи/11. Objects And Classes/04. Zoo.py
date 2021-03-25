# Create a class Zoo. It should have a class attribute called __animals that stores the total
# count of the animals in the zoo. The __init__ method should only receive the name of the zoo.
# There you should also create 3 empty lists (mammals, fishes, birds). The class should also have 2 more methods:
# •	add_animal(species, name) - based on the species adds the name to the corresponding list
# •	get_info(species) - based on the species returns a string in the following format:
# "{Species} in {zoo_name}: {names}" and on another line "Total animals: {total_animals}"
# On the first line you will receive the name of the zoo. On the second line you will receive
# number n. On the next n lines you will receive animal info in the format: "{species} {name}".
# Add the animal to the zoo to the corresponding list. The "species" command will be mammal, fish
# or bird. On the final line you will receive a spеcies. At the end, print all the info for that
# 	species and the total count of animals.
class Zoo:
	def __init__(self, name):
		self.name = name
		self.mammals = []
		self.fish = []
		self.birds = []
		self.total_animals = 0



	def add_animal(self, species , name):
		if species == "mammal":
			self.mammals.append(name)
		elif species == "fish":
			self.fish.append(name)
		elif species == "bird":
			self.birds.append(name)
		self.total_animals += 1

	def get_info(self, species):
		result = None
		if species == "mammal":
			result = f'Mammals in {self.name}: {", ".join(self.mammals)}'
		elif species == "fish":
			result = f'Fishes in {self.name}: {", ".join(self.fish)}'
		elif species == "bird":
			result = f'Birds in {self.name}: {", ".join(self.birds)}'
		return result

	def get_final_info(self):
		return f'Total animals: {self.total_animals}'


name_of_zoo = input()
zoo = Zoo(name_of_zoo)
times = int(input())
for time in range(times):
	kind, animal = input().split()
	zoo.add_animal(kind, animal)
our_type = input()
print(zoo.get_info(our_type))
print(zoo.get_final_info())













