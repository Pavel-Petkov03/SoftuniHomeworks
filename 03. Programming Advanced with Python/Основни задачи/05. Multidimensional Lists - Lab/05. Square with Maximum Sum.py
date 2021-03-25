# Write a program that read a matrix from console. Find biggest sum of 2x2 submatrix and print it to console.
# Input
# On first line you will get matrix sizes in format rows, columns.
# One next rows lines you will get elements for each column separated with coma.
# Output
# Print biggest top-left square, which you find and sum of its elements.


row_, col_ = list(map(int, input().split(', ')))
matrix = [list(map(int, input().split(', '))) for c in range(row_)]
max_num = []
max_sum = 0
sub_m = None
for row in range(row_ - 1):
	for col in range(col_ - 1):
		sub_m = [[matrix[row][col], matrix[row][col + 1]], [matrix[row + 1][col], matrix[row + 1][col + 1]]]
		if sum([sum(c)for c in sub_m]) > sum([sum(c) for c in max_num]):
			max_num = sub_m
			max_sum = sum([sum(c) for c in max_num])
for index in max_num:
	print(' '.join(map(str, index)))
print(max_sum)




