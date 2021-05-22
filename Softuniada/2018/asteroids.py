result = []


def validate(m, r, c):
    if r + 1 in range(len(m)) and m[r + 1][c] == '1' or c + 1 in range(len(m[row])) and m[row][
        c + 1] == '1' or r - 1 in range(len(m)) and m[r - 1][c] == '1' or c - 1 in range(len(m[r])) and m[r][
        c - 1] == '1':
        return True
    return False


def add_size(c):
    global result
    wanted_index = None
    values = [c[1] for c in result]
    if c in values:
        for ge in range(len(result)):
            if result[ge][1] == c:
                wanted_index = ge
                break
        result[wanted_index][0] += 1
    else:
        result.append([1, c])


def calculate_groups(m):
    counter = 1
    for row in range(len(m)):
        for col in range(len(m[row])):
            if m[row][col] == '1':
                if validate(m, row, col):
                    m[row][col] = '0'
                    counter += 1
                else:
                    add_size(counter)
                    counter = 1

    temp = result.copy()
    result.clear()
    return temp


command = input()
while command != 'end':
    g, x = list(map(int, command.split('x')))
    matrix = []
    for row in range(g):
        matrix.append(list(input()))
    r = calculate_groups(matrix)
    total = 0
    for j in r:
        print('x'.join([str(c) for c in j]))
        total += j[0]
    print(f'Total {total}')

    command = input()
