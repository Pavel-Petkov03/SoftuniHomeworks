n = int(input())
for rows in range(1, n + 1):
    for columns in range(1, n + 1):
        if columns == 1 and rows == 1 or columns == n and rows == 1 or rows == n and columns == 1\
                or columns == n and rows == n:
            print("+", end=' ')
        elif (1 < rows <= n and columns == 1) or (1 < rows <= n and columns == n):
            print("|", end=' ')
        else:
            print("-", end=' ')
        print(end='')
    print()
