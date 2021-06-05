n = int(input())
matrix = [input().split() for _ in range(n)]
coins = 0
loose = False

cord = []

def find_person(m):
    for r in range(len(m)):
        for c in range(len(m[r])):
            if m[r][c] == 'P':
                return [r, c]

def move(cmd , pos):
    global cord
    if cmd  == 'left':
        pos[1] -= 1
    elif cmd == 'right':
        pos[1] += 1
    elif cmd == 'up':
        pos[0] -= 1
    elif cmd == 'down':
        pos[0] += 1
    cord.append(pos)
    return pos
initial_r, initial_c = find_person(matrix)
while coins < 100:
    command = input()
    initial_r, initial_c = move(command, [initial_r, initial_c])
    if initial_r not in range(n) or initial_c not in range(n) or matrix[initial_r][initial_c] == 'X':
        loose = True
        coins *= 0.5
        coins = int(coins)
        cord.pop()
        break
    coins += int(matrix[initial_r][initial_c])

if not loose:
    print(f'You won! You\'ve collected {coins} coins.')
else:
    print(f'Game over! You\'ve collected {coins} coins.')

print('Your path:')
[print(f'[{c}, {d}]') for c, d in cord]
