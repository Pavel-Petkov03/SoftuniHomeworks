# Write a program that reads a string, matrix, from the console and perform certain operations with
# 	its elements. User input is provided in a similar way like in the problems above - first you read
# 	the dimensions and then the data.
# Your program should receive commands in format: "swap row1 col1 row2 col2" where row1, row2, col1, col2
# are coordinates in the matrix. For a command to be valid, it should start with the "swap" keyword along
# with four valid coordinates (no more, no less). You should swap the values at the given
# and print the matrix at each step
# (thus you'll be able to check if the operation was performed correctly).
# If the command is not valid
# (doesn't contain the keyword "swap", has fewer or more coordinates entered or the given coordinates do not exist), '
# 'print "Invalid input!" and move on to the next command. Your program should finish when the string "END" is entered.


initial_row , initial_col = list(map(int, input().split()))
matrix = [input().split() for c in range(initial_row)]
command = input()
while command != 'END':
	command = command.split()
	if len(command) == 5:
		swap = command[0]
		row1, col1, row2, col2 = list(map(int,command[1:]))
		if row1 in range(len(matrix)) and row2 in range(len(matrix)) and col1 in range(len(matrix[initial_row-1])) and col2 \
			in range(len(matrix[initial_row-1])) and swap == 'swap':
			matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
			[print(' '.join(c)) for c in matrix]
		else:
			print('Invalid input!')
	else:
		print( 'Invalid input!' )
	command = input()
