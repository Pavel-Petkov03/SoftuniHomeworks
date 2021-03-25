data = [int(c) for c in input().split()]
command = input()
while command != 'Mort':
	command = command.split()
	if command[0] == 'Add':
		data.append(int(command[1]))
	elif command[0] == 'Remove':
		value = int(command[1])
		if value in data:
			data.remove(value)
	elif command[0] == 'Replace':
		value = int(command[1])
		replacement = int(command[2])
		if value in data:
			pos = data.index(value)
			data[pos] = replacement
	elif command[0] == 'Collapse':
		value = int(command[1])
		data = [c for c in data if c >= value]
	command = input()
print(' '.join([str(c) for c in data]))