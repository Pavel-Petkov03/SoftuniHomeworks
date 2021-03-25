# Write a program that reads N, a number representing the rows and cols of a matrix. On the next N lines, you
# will receive rows of the matrix. Each row consists of ASCII characters. After that, you will receive a symbol.
# Find the first occurrence, starting from the top left, of that symbol in the matrix and print its position in the
# format: "({row}, {col})". If there is no such symbol print an error message "{symbol} does not occur in the matrix"

matrix = [[d for d in input()] for c in range(int(input()))]
char = input()
is_not_fill = True
for row in range(len(matrix)):
	if char in matrix[row]:
		print((row, matrix[row].index(char)))
		is_not_fill = False
		break
if is_not_fill:
	print(f'{char} does not occur in the matrix')