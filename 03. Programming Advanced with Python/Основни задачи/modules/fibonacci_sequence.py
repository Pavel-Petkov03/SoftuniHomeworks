def create_sequence(i):
	new_list = []
	for j in range(i):
		if j <= 1:
			new_list.append(j)
		else:
			new_list.append(new_list[-1]+new_list[-2])
	return new_list


def locate_num(location, sequence):
	if location in sequence:
		print(f"The number - {location} is at index {sequence.index(location)}")
	else:
		print(f"The number {location} is not in the sequence")


def do_commands_while_end():
	command = input()
	seq = []
	while command != 'Stop':
		command = command.split()
		if command[0] == 'Create':
			seq = create_sequence(int(command[2]))
			print(' '.join(list(map(str, seq))))
		elif command[0] == 'Locate':
			locate_num(int(command[1]), seq)
		command = input()


do_commands_while_end()


