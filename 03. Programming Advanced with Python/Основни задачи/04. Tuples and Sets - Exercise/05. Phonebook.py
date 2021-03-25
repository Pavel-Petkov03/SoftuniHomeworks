# Write a program that receives info from the console about people and their phone numbers.
# You are free to choose the way the data is entered; each entry should have a name and a number
# (both strings). If you receive a name that already exists in the phonebook, update its number.
# After filling the phonebook, you will receive a number – N. Your program should be able to perform a
# search of a contact by name and print her details in format "{name} -> {number}". In case the contact
# isn't found, print "Contact {name} does not exist."


command = input()
my_dict = {}
while not command.isdigit():
	name, phone = command.split('-')
	my_dict[name] = phone
	command = input()
for c in range(int(command)):
	new_name = input()
	if new_name in my_dict:
		print(f"{new_name} -> {my_dict[new_name]}")
	else:
		print(f"Contact {new_name} does not exist.")


