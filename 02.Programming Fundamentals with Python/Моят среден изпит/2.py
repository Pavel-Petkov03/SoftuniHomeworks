my_list = []
command = input()
while command != 'end':
	command = command.split()
	if command[0] == 'Chat':
		my_list.append(command[1])
	elif command[0] == 'Delete':
		if command[1] in my_list:
			pos = my_list.index(command[1])
			my_list.pop(pos)
	elif command[0] == 'Edit':
		if command[1] in my_list:
			pos = my_list.index(command[1])
			my_list[pos] = command[2]

	elif command[0] == 'Spam':
		for c in command[1:]:
			my_list.append(c)

	elif command[0] == 'Pin':
		if command[1] in my_list:
			pos = my_list.index(command[1])
			my_list.append(my_list.pop(pos))

	command = input()

print('\n'.join(my_list))