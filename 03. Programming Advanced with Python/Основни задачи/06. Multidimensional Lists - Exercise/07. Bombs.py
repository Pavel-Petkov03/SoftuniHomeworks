# You will be given a square matrix of integers, each integer separated by a single space, and each row on a new line.
# Then on the last line of input you will receive indexes - coordinates to several cells separated by a single space,
# in the following format: row1,column1  row2,column2  row3,column3…
# On those cells there are bombs. You must detonate every bomb, in the order they were given. When a bomb explodes,
# it deals damage equal to its own integer value, to all the cells around it (in every direction and in all diagonals).
# One bomb can't explode more than once and after it does, its value becomes 0. When a cell's value reaches 0 or below,
# it dies. Dead cells can't explode.
# You must print the count of all alive cells and their sum. Afterwards, print the matrix with all its cells
# (including the dead ones).
# Input
# •	On the first line, you are given the integer N - the size of the square matrix.
# •	The next N lines holds the values for every row - N numbers separated by a space.
# •	On the last line, you will receive the coordinates of the cells with the bombs in the format described above.
# Output
# •	On the first line, you need to print the count of all alive cells in the format:
# "Alive cells: {aliveCells}"
# •	On the second line, you need to print the sum of all alive cell in the format:
# "Sum: {sumOfCells}"
# •	In the end print the matrix. The cells must be separated by a single space.
#
# Constraints
# •	The size of the matrix will be between [0…1000].
# •	The bomb coordinates will always be in the matrix.
# •	The bomb's values will always be greater than 0.
# •	The integers of the matrix will be in range [1…10000].
n = int(input())
matrix = [list(map(int, input().split())) for c in range(n)]
explosion_coordinates = [tuple(map(int, c.split(','))) for c in input().split()]


def explosion(r, c, m):
	removal = m[r][c]
	m[r][c] = 0
	row_pos = [-1, -1, -1, 0, 0, 1, 1, 1]
	col_pos = [-1, 0, 1, -1, 1, -1, 0, 1]
	for find in range(8):
		find_row = r + row_pos[find]
		find_col = c + col_pos[find]
		if 0 <= find_row < len(m) and 0 <= find_col < len(m[0]) and m[find_row][find_col] > 0:
			m[find_row][find_col] -= removal
	return m


def alive_cells(m):
	return len([c for a in m for c in a if c > 0])


def sum_alive(m):
	return sum([c for a in m for c in a if c > 0])



for tup in explosion_coordinates:
	exp_row, exp_col = tup
	place = matrix[exp_row][exp_col]
	if place > 0:
		matrix = explosion(exp_row, exp_col, matrix)

print(f'Alive cells: {alive_cells(matrix)}')
print(f'Sum: {sum_alive(matrix)}')
[print(' '.join(list(map(str, c))))for c in matrix]
