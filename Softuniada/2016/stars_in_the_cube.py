from itertools import combinations


def check_if_all_eq(l, max_value):
    for k in l:
        if not sum(k) == max_value:
            return False
    return True


is_true = False

matrix = []
n = int(input())
for _ in range(n):
    matrix.append(list(map(int, input().split())))

for l in matrix:
    for i in range(1, len(l)):
        initial_list = list(combinations(l, i))
        max_value = sum(l) / 3
        exp = check_if_all_eq(initial_list, max_value)
        if exp is True:
            is_true = True
            print('True')
            break
    if not is_true:
        print('False')
    is_true = False
