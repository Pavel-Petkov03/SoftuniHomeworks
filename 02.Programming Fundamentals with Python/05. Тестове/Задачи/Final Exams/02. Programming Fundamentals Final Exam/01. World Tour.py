# You are a world traveller and your next goal is to make a world tour. In order to do that,
# you have to plan out everything first. To start with, you would like to plan out all of
# your stops where you will have a break.
# On the first line you will be given a string containing all of your stops. Until you receive
# the command "Travel", you will be given some commands to manipulate that initial string. The commands can be:
# •	Add Stop:{index}:{string} – insert the given string at that index only if the index is valid
# •	Remove Stop:{start_index}:{end_index} – remove the elements of the string from the starting
# index to the end index (inclusive) if both indices are valid
# •	Switch:{old_string}:{new_string} – if the old string is in the initial string, replace it with
# the new one. (all occurrences)
# Note: After each command print the current state of the string
# After the "Travel" command, print the following: "Ready for world tour! Planned stops: {string}"
# Input / Constraints
# •	JavaScript: you will receive a list of strings
# Output
# •	Print the proper output messages in the proper cases as described in the problem description

our_str = input()
command = input()
while command != 'Travel':
	task, first, second = command.split(":")
	if task == 'Add Stop':
		if int(first) in range(len(our_str)):
			our_str = [c for c in our_str]
			our_str.insert(int(first), second)
			our_str = ''.join(our_str)
	elif task == 'Remove Stop':
		if int(first) in range(len(our_str)) and int(second) in range(len(our_str)):
			our_str = [c for c in our_str]
			our_str = ''.join(our_str[:int(first)] + our_str[int(second) + 1:])
	elif task == 'Switch':
		if first in our_str:
			our_str = our_str.replace(first, second)

	print(our_str)
	command = input()
print(f"Ready for world tour! Planned stops: {our_str}")

