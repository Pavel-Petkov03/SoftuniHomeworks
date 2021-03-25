# Create a function called even_odd that can receive different amount of numbers and a command at the end. The
# command can be "even" or "odd". Filter the numbers depending on the command and
# return them in a list. Submit only the function in the judge system.
def even_odd(*args):
	command = args[-1]
	doing_dict = {'odd': [c for c in args[:-1] if c % 2 != 0], 'even': [c for c in args[:-1] if c % 2 == 0]}
	return doing_dict[command]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))


