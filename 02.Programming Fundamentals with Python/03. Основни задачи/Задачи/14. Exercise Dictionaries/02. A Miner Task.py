# You will be given a sequence of strings, each on a new line. Every odd line on the console is
# representing a resource (e.g. Gold, Silver, Copper, and so on) and every even – quantity.
# Your task is to collect the resources and print them each on a new line.
# Print the resources and their quantities in the following format:
# {resource} –> {quantity}
# The quantities will be in the range [1 … 2 000 000 000]
our_dictionary = {}
command = input()
while command != "stop":
	resource = command
	quantity = int(input())
	if resource in our_dictionary:
		our_dictionary[resource] += quantity
	else:
		our_dictionary[resource] = quantity
	command = input()
for resource, quantity in our_dictionary.items():
	print(f'{resource} -> {quantity}')

