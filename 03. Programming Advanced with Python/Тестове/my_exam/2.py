matrix = [input().split() for c in range(5)]
n = int(input())
cord = []
t = 0


def find_x(m):
    c = 0
    for row in range(len(m)):
        for col in range(len(m[row])):
            if m[row][col] == 'x':
                c += 1
    return c


c = find_x(matrix)


def find_person(m):
    for row in range(len(m)):
        for col in range(len(m[row])):
            if m[row][col] == 'A':
                return row, col


def do(cmd, r, c, m):
    global t
    global cord
    if len(cmd) == 3:
        _, poss, num = cmd
        num = int(num)
        if poss == 'right' and c + num < len(m) and m[r][c+num] == '.':
            c += num
        elif poss == 'left' and c - num >= 0 and m[r][c-num] == '.':
            c -= num
        elif poss == 'up' and r - num >= 0 and m[r-num][c] == '.':
            r -= num
        elif poss == 'down' and r + num < len(m) and m[r+num][c] == '.':
            r += num

    else:
        _, poss = command
        if poss == 'left':
            for find in range(c, -1, -1):
                if m[r][find] == 'x':
                    m[r][find] = '.'
                    t += 1
                    cord.append(f"[{r}, {find}]")
                    break
        elif poss == 'right':
            for find in range(c, len(m)):
                if m[r][find] == 'x':
                    m[r][find] = '.'
                    t += 1
                    cord.append(f"[{r}, {find}]")
                    break
        elif poss == 'up':
            for find in range(r, -1, -1):
                if m[find][c] == 'x':
                    m[find][c] = '.'
                    t += 1
                    cord.append(f"[{find}, {c}]")
                    break
        elif poss == 'down':
            for find in range(r, len(m)):
                if m[find][c] == 'x':
                    m[find][c] = '.'
                    t += 1
                    cord.append(f"[{find}, {c}]")
                    break
    return r, c, m


start_r, start_c = find_person(matrix)

for _ in range(n):
    if find_x(matrix) == 0:
        break
    command = input().split()
    start_r, start_c, matrix = do(command, start_r, start_c, matrix)

if c == len(cord):
    print(f'Training completed! All {c} targets hit.')
else:
    print(f'Training not completed! {c - len(cord)} targets left.')
[print(c) for c in cord]