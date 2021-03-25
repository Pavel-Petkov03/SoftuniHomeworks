# Input / Constraints
# You will receive a journal with some Collecting items, separated with ', '
# (comma and space). After that, until receiving "Craft!" you will be receiving different commands.
# Commands (split by " - "):
# •	"Collect - {item}" – Receiving this command, you should add the given item
# in your inventory. If the item already exists, you should skip this line.
# •	"Drop - {item}" – You should remove the item from your inventory, if it exists.
# •	"Combine Items - {oldItem}:{newItem}" – You should check if the old item exists,
# if so, add the new item after the old one. Otherwise, ignore the command.
# •	"Renew – {item}" – If the given item exists, you should change its position and put it last in your inventory.
# Output
# After receiving "Craft!" print the items in your inventory, separated by ", " (comma and space).
def stuff_manipulation(array):
	def collect(item):
		if item not in array:
			array.append(item)
		return array

	def drop(item):
		if item in array:
			array.remove(item)
		return array

	def combine(old_and_new):
		old, new = old_and_new.split(":")
		if old in array:
			array.insert(array.index(old) + 1, new)
		return array

	def renew(item):
		if item in array:
			array.remove(item)
			array.append(item)
		return array

	array = array.split(", ")
	command = input()
	while command != "Craft!":
		command = command.split(" - ")
		if command[0] == 'Collect':
			array = collect(command[1])
		elif command[0] == "Drop":
			array = drop(command[1])
		elif command[0] == "Combine Items":
			array = combine(command[1])
		elif command[0] == "Renew":
			command = renew(command[1])
		command = input()
	return ", ".join(array)


our_array = input()
print(stuff_manipulation(our_array))




