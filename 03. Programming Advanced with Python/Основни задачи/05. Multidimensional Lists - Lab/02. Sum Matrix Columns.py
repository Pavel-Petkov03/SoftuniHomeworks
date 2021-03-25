# Write a program that reads a matrix from the console and prints the sum for each column. On the first line,
# you will get the matrix's rows. On the next rows, you will get elements for each column separated with a space.

row, col = map(int, input().split(', '))
matrix = [list(map(int, input().split())) for c in range(row)]
for column in range(col):
	my_sum = 0
	for row_ in range(row):
		my_sum += matrix[row_][column]
	print(my_sum)




