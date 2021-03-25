# You will be given an integer n for the size of the mines field with square shape and another
# one for the number of bombs that you have to place in the field. On the next n lines, you will
# receive the position for each bomb.
# Your task is to create the game field placing the bombs at the correct positions and mark them
# with "*", and calculate the numbers in each cell of the field. Each cell represents a number of
# all bombs directly near it (up, down, left, right and the 4 diagonals).

import re


def increase_function(m, r, c):
    final = 0
    row_template = [0, 1, 1, 1, 0, -1, -1, -1]
    col_template = [1, 1, 0, -1, -1, -1, 0, 1]
    for find in range(8):
        current_r = row_template[find] + r
        current_c = col_template[find] + c
        if current_r in range(len(m)) and current_c in range(len(m[0])) and m[current_r][current_c] == '*':
            final += 1
    return final


matrix_length = int(input())
matrix = [[0] * matrix_length for c in range(matrix_length)]
bombs = int(input())
for bomb in range(bombs):
    row, col = list(map(int, re.findall('\d+', input())))
    if row in range(len(matrix)) and col in range(len(matrix[row])):
        matrix[row][col] = '*'

for row_check in range(len(matrix)):
    for col_check in range(len(matrix[row_check])):
        if matrix[row_check][col_check] != '*':
            matrix[row_check][col_check] = increase_function(matrix, row_check, col_check)

[print(' '.join(list(map(str, c)))) for c in matrix]
