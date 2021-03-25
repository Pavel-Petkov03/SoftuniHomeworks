# Write a program that reads a matrix from the console. On the first line, you will get the matrix's rows.
# On next rows lines, you will get elements for each column, separated with space. You will be receiving
# commands in the following format:
# •	Add {row} {col} {value} – Increase the number at the given coordinates with the value.
# •	Subtract {row} {col} {value} – Decrease the number at the given coordinates by the value.
# If the coordinate is invalid, you should print "Invalid coordinates".
# When you receive "END", you should print the matrix and stop the program.


matrix = [list(map(int, input().split())) for _ in range(int(input()))]
command = input()
while command != 'END':
	task, row, col, value = command.split()
	row, col, value = int(row), int(col), int(value)
	if task == 'Add':
		if row in range(len(matrix)) and col in range(len(matrix[0])):
			matrix[row][col] += value
		else:
			print('Invalid coordinates')
	elif task == 'Subtract':
		if row in range(len(matrix)) and col in range(len(matrix[0])):
			matrix[row][col] -= value
		else:
			print('Invalid coordinates')
	command = input()

[print(' '.join(list(map(str, text)))) for text in matrix]






