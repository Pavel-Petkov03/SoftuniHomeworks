# Write a program that finds the difference between the sums of the square matrix diagonals (absolute value).
row = int(input())
matrix = [list(map(int, input().split())) for c in range(row)]
first_d = 0
second_d = 0
col_ = 0
for row_ in range(row):
	first_d += matrix[row_][row_]
for row_ in reversed(range(row)):
	second_d += matrix[row_][col_]
	col_ += 1

print(abs(first_d - second_d))
