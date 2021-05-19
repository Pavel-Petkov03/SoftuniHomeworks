from copy import deepcopy


def sum_(m, r, c):
    counter = 0
    if m + 1 in range(n) and new_cube[m + 1][r][c] != bad_item:
        counter += new_cube[m + 1][r][c]
    if m - 1 in range(n) and new_cube[m - 1][r][c] != bad_item:
        counter += new_cube[m - 1][r][c]
    if r + 1 in range(n) and new_cube[m][r + 1][c] != bad_item:
        counter += new_cube[m][r + 1][c]
    if r - 1 in range(n) and new_cube[m][r - 1][c] != bad_item:
        counter += new_cube[m][r - 1][c]
    if c + 1 in range(n) and new_cube[m][r][c + 1] != bad_item:
        counter += new_cube[m][r][c + 1]
    if c - 1 in range(n) and new_cube[m][r][c - 1] != bad_item:
        counter += new_cube[m][r][c - 1]
    return counter


n = int(input())
cube = [[] for _ in range(n)]
for _ in range(n):
    row = input().split(' | ')
    for col in row:
        min_list = ''.join(col).split()
        cube[_].append(list(map(int, min_list)))

replaced = 0


r_m, r_r, r_c = list(map(int, input().split()))
new_cube = [[] for _ in range(n)]
for row in range(n):
    for matrix in range(n):
        new_cube[row].append(cube[matrix][row])

bad_item = new_cube[r_m][r_r][r_c]
result_cube = deepcopy(new_cube)
for m in range(n):
    for r in range(n):
        for c in range(n):
            if new_cube[m][r][c] == bad_item:
                result_cube[m][r][c] = sum_(m, r, c)
                replaced += 1

print(f'Wrong values found and replaced: {replaced}')
[print(' '.join([str(c) for c in row])) for matrix in result_cube for row in matrix]
