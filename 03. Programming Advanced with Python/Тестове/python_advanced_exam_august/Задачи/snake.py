# You will be given an integer n for the size of the snake territory with square shape. On the next n lines,
# you will receive the rows of the territory. The snake will be placed on a random position, marked with the
# letter 'S'. On random positions there will be food, marked with '*'. There might also be a lair on the territory.
# The lair has two burrows. They are marked with the letter - 'B'. All of the empty positions will be marked with '-'.
# Each turn, you will be given command for the snake’s movement. When the snake moves it leaves a trail marked with '.'
# Move commands will be: "up", "down", "left", "right".
# If the snake moves to a food, it eats the food and increases the food quantity with one.
# If it goes inside of a burrow, it goes out on the position of the other burrow and then both burrows
# disappear. If the snake goes out of its territory, it loses, can't return back and the program ends.
# The snake needs at least 10 food quantity to win.
# When the snake has gone outside of its territory or has eaten enough food, the game ends.
# Input
# •	On the first line, you are given the integer n – the size of the square matrix.
# •	The next n lines holds the values for every row.
# •	On each of the next lines you will get a move command.
# Output
# •	On the first line:
# o	If the snake goes out of its territory, print: "Game over!"
# o	If the snake eat enough food, print: "You won! You fed the snake."
# •	On the second line print all food eaten: "Food eaten: {food quantity}"
# •	In the end print the matrix.
# Constraints
# •	The size of the square matrix will be between [2…10].
# •	There will always be 0 or 2 burrows, marked with - 'B'.
# •	The snake position will be marked with 'S'.
# •	The snake will always either go outside its territory or eat enough food.
# •	There will be no case in which the snake will go through itself.



n = int(input())
snake_lair = [list(input()) for c in range(n)]
final_res = 0

def start(m):
    for r in range(len(m)):
        for c in range(len(m[r])):
            if m[r][c] == 'S':
                return r, c


def check_for_item(m, r, c):
    if m[r][c] == '*':
        global final_res
        final_res += 1
    elif m[r][c] == 'B':
        m[r][c] = '.'
        for row in range(len(m)):
            for col in range(len(m[row])):
                if m[row][col] == 'B':
                    r, c = row, col
                    m[r][c] = 'S'
                    return m,r,c

    return m, r, c


def move(m, r, c, cmd):
    m[r][c] = '.'
    if cmd == 'left':
        c -= 1
        m,r,c = check_for_item(m,r,c)
    elif cmd == 'right':
        c += 1
        m, r, c = check_for_item(m, r, c)
    elif cmd == 'up':
        r -= 1
        m, r, c = check_for_item(m, r, c)
    elif cmd == 'down':
        r += 1
        m, r, c = check_for_item(m, r, c)
    m[r][c] = 'S'
    return m,r,c

def validate(m,r,c,cmd):
    if cmd == 'left':
         c -= 1
    elif cmd == 'right':
        c += 1
    elif cmd == 'up':
        r -= 1
    elif cmd == 'down':
        r += 1
    if r in range(len(m)) and c in range(len(m[0])):
        return True
    return False
entry_row, entry_col = start(snake_lair)
is_over = False
while final_res != 10:
    command = input()
    if validate(snake_lair,entry_row,entry_col,command):
        snake_lair,entry_row,entry_col = move(snake_lair,entry_row,entry_col,command)
    else:
        snake_lair[entry_row][entry_col] = '.'
        is_over = True
        break

if is_over:
    print('Game over!')
else:
    print('You won! You fed the snake.')
print(f'Food eaten: {final_res}')
[print(''.join(c)) for c in snake_lair]
