# Chess is the oldest game, but it is still popular these days. For this task, we will
# use only one chess piece - the Knight.
# The knight moves to the nearest square but not on the same row, column, or diagonal.
# (This can be thought of as moving two squares horizontally, then one square vertically,
# or moving one square horizontally then two squares vertically - i.e. in an "L" pattern.)
# The knight game is played on a board with dimensions N x N.
# You will receive a board with K for knights and '0' for empty cells. Your task is to
# remove knights until there are no knights left that can attack one another.
# Input
# -	On the first line, you will receive the N size of the board
# -	On the next N lines, you will receive strings with Ks and 0s.
# Output
# Print a single integer with the minimum number of knights that needs to be removed


initial_rows = int(input())
matrix = [list(input()) for c in range(initial_rows)]
kill_counter = 0

def find_biggest_killer(place_row, place_col, m): # initial_place = matrix[place_row][place_col]
	row_movement = [-2, - 2, -1, 1, 2, 2, 1, -1]
	col_movement = [-1, 1, 2, 2, 1, -1, -2, -2]
	biggest_counter = 0
	for find in range(8):
		row_moves_at = place_row + row_movement[find]
		col_moves_at = place_col + col_movement[find]
		if 0 <= row_moves_at < len(m) and 0 <= col_moves_at < len(m[0]):
			if 'K' == m[row_moves_at][col_moves_at]:
				biggest_counter += 1
	return biggest_counter, (place_row, place_col)


def find_biggest_killer_from_all_killers(big_massive):
	big_place = tuple()
	max_value = -1
	for value, pos in big_massive:
		if value > max_value:
			max_value = value
			big_place = pos
	return max_value, big_place


while True:
	biggest_massive = []
	for row in range(len(matrix)):
		for col in range(len(matrix[row])):
			if matrix[row][col] == 'K':
				biggest_massive.append(find_biggest_killer(row, col, matrix))
	counter_kill, coordinate = find_biggest_killer_from_all_killers(biggest_massive)
	if counter_kill == 0:
		break
	else:
		kill_row, kill_col = coordinate
		matrix[kill_row][kill_col] = 0
		kill_counter += 1


print(kill_counter)

