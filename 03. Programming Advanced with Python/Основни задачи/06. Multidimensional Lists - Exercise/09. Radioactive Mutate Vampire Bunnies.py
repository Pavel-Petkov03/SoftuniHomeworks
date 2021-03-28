# Browsing through GitHub, you come across an old JS Basics teamwork game. It is about very nasty bunnies
# that multiply extremely fast. There's also a player that has to escape from their lair. You really like the
# game, so you decide to port it to Python because that's your language of choice. The last thing that is left is
# the algorithm that decides if the player will escape the lair or not.
# First, you will receive a line holding integers N and M, which represent the rows and columns in the lair. Then
# you receive N strings that can consists only of ".", "B", "P". The bunnies are marked with "B", the player is marked
# with "P", and everything else is free space, marked with a dot ".". They represent the initial state of the lair.
# There will be only one player. Then you will receive a string with commands such as LLRRUUDD - where each letter
# represents the next move of the player (Left, Right, Up, Down).
# After every step, each of the bunnies spread to the up, down, left and right (neighboring cells marked as "."
# changes their value to "B"). If the player moves to a bunny cell or a bunny reaches the player, the player has
# died. If the player goes out of the lair without encountering a bunny, the player has won.
# When the player dies or wins, the game ends. All the activities for this turn continue (e.g. all the bunnies
# spread normally), but there are no more turns. There will be no stalemates where the moves of the player end
# before he dies or escapes.
# Finally, print the final state of the lair with every row on a separate line. On the last line, print either
# "dead: {row} {col}" or "won: {row} {col}". Row and col are the coordinates of the cell where the player has
# died or the last cell he has been in before escaping the lair.
# Input
# •	On the first line of input, the numbers N and M are received - the number of rows and columns in the lair
# •	On the next N lines, each row is received in the form of a string. The string will contain only ".", "B",
# "P". All strings will be the same length. There will be only one "P" for all the input
# •	On the last line, the directions are received in the form of a string, containing "R", "L", "U", "D"
# Output
# •	On the first N lines, print the final state of the bunny lair
# •	On the last line, print the outcome - "won:" or "dead:" + {row} {col}
# Constraints
# •	The dimensions of the lair are in range [3…20]
# •	The directions string length is in range [1…20]


from copy import deepcopy


def dead_situation(r, c, m):
	if m[r][c] == 'B':
		return True
	return False


def won_situation(r, c, m, command):
	if command == 'U' and r == 0:
		return True
	elif command == 'D' and r == len(m) - 1:
		return True
	elif command == 'L' and c == 0:
		return True
	elif command == 'R' and c == len(m[0]) - 1:
		return True
	return False


def entry_pos(m):
	for r in range(len(m)):
		for c in range(len(m[0])):
			if matrix[r][c] == 'P':
				matrix[r][c] = '.'
				return r, c


def command_parsing(r, c, initial_command):
	if initial_command == 'U':
		r -= 1
	elif initial_command == 'D':
		r += 1
	elif initial_command == 'L':
		c -= 1
	elif initial_command == 'R':
		c += 1
	return r, c


def moving_p(place_row, place_col, cmd_line, m):
	for cmd in cmd_line:
		m = bunny_producing(m)
		if won_situation(place_row, place_col, m, cmd):
			result = print_matrix(m)
			result += f'won: {place_row} {place_col}'
			return result
		place_row, place_col = command_parsing(place_row, place_col, cmd)
		if dead_situation(place_row, place_col, m) is True:
			result = print_matrix(m)
			result += f'dead: {place_row} {place_col}'
			return result


def bunny_producing(m):
	row_placeholder = [0, -1, 0, 1]
	col_placeholder = [-1, 0, 1, 0]
	new_matrix = deepcopy(m)
	for row in range(len(m)):
		for col in range(len(m[0])):
			if m[row][col] == 'B':
				for find in range(4):
					row_finder = row + row_placeholder[find]
					col_finder = col + col_placeholder[find]
					if row_finder in range(len(m)) and col_finder in range(len(m[0])):
						matrix[row_finder][col_finder] = 'B'
	return new_matrix


def print_matrix(m):
	result = ''
	for c in m:
		result += ''.join(c)
		result += '\n'
	return result


initial_row, initial_col = list(map(int, input().split()))
matrix = [list(input()) for c in range(initial_row)]
entry_row, entry_col = entry_pos(matrix)
command_line = list(input())
print(moving_p(entry_row, entry_col, command_line, matrix))

