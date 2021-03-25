# Using a nested list comprehension, write a program that reads NxN matrix, finds its
# diagonals, prints them and their sum as shown below.



initial_rows = int(input())
matrix = [list(map(int, input().split(', '))) for _ in range(initial_rows)]
f_d = 0
s_d = 0
col = len(matrix[0]) - 1
f_d_list = []
s_d_list = []
for row in range(initial_rows):
	f_d += matrix[row][row]
	f_d_list.append(matrix[row][row])
	s_d += matrix[row][col]
	s_d_list.append(matrix[row][col])
	col -= 1
print(f'First diagonal: {", ".join(list(map(str , f_d_list)))}. Sum: {f_d}')
print(f'Second diagonal: {", ".join(list(map(str , s_d_list)))}. Sum: {s_d}')
