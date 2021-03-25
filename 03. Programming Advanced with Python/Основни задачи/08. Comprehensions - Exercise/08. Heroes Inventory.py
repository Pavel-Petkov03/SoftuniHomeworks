# Using a comprehension, write a program that receives a hero's names and items that
# need to be added in their inventory (item name and item cost). Print the total
# amount of items with their total cost for each hero.
# Input
# •	On the first line, you will receive the names of the heroes separated by comma and space ", "
# •	On the next lines until the command "End", you will be given items with their cost in the following format:
# "{name}-{item}-{cost}". If an item already exists in the hero's inventory - ignore it.
# Output
# •	For each hero, print his name, the total items and the total cost of the items in the format: \
# 	"{name} -> Items: {items_count}, Cost: {items_cost}"

my_dict = {c: [0, 0, []] for c in input().split(', ')}


def taking(d, c):
	name, item, cost = c.split("-")
	if item not in d[name][2]:
		d[name][0] += 1
		d[name][1] += int(cost)
		d[name][2].append(item)
	return d


command = input()
while command != 'End':
	my_dict = taking(my_dict, command)
	command = input()

[print(f'{key} -> Items: {value[0]}, Cost: {value[1]}')for key, value in my_dict.items()]
