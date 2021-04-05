n = int(input())
for i in range(n - 1):
    for j in range(2 * n - 1):
        if j + 1 == n - i or j + 1 == n + i:
            print('*', end='')
        elif j + 1 > n - i and j + 1 < n + i:
            print(' ', end='')
        elif j + 1 < n - i or j + 1 > n - i:
            print('.', end='')
    print()
for last in range(2 * n - 1):
    if last % 2 == 0:
        print('*', end='')
    else:
        print(' ', end='')
print()
for row in range(n):
    for col in range(2 * n - 1):
        if (row == 0 and col == 0) or (col == 2 * n - 2 and row == 0) or (row == n-1 and col == 0) or (
                row == n-1 and col == 2 * n - 2):
            print('+', end='')
        elif row == 0 or row == n-1:
            print('-', end='')
        elif col == 0 or col == 2*n-2:
            print('|', end='')
        else:
            print(' ',end='')
    print()
