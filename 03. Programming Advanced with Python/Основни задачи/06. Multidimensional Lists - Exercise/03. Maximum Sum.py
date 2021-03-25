# Write a program that reads a rectangular integer matrix of size N x M and find the
# square 3 x 3 that has maximal sum of its elements.
# Input
# •	On the first line, you will receive the rows N and columns M. On the next N lines
# you will receive each row with its columns
# Output
# •	Print the elements of the 3 x 3 square as a matrix, along with their sum


initial_row, initial_col = list(map(int, input().split()))
matrix = [list(map(int, input().split())) for c in range(initial_row)]
max_sum = 0
max_matrix = []
for row in range(initial_row - 2):
	for col in range(initial_col - 2):
		sub_matrix = []
		for sub_row in range(row, row + 3):
			temp = []
			for sub_col in range(col, col + 3):
				temp.append(matrix[sub_row][sub_col])
			sub_matrix.append(temp)
		if sum([sum(c) for c in sub_matrix]) > max_sum:
			max_sum = sum([sum(c) for c in sub_matrix])
			max_matrix = sub_matrix.copy()
print(f'Sum = {max_sum}')
[print(' '.join(list(map(str, c)))) for c in max_matrix]

