# You will be given a string. Then, you will be given an integer N for the size of the field with square shape.
# On the next N lines, you will receive the rows of the field. The player will be placed on a random position,
# marked with "P". On random positions there will be letters. All of the empty positions will be marked with "-".
# Each turn you will be given commands for the player’s movement. If he moves to a letter, he consumes it, concatеnates
# it to the initial string and the letter disappears from the field. If he tries to move outside of the field, he is
# punished - he loses the last letter in the string, if there are any, and the player’s position is not changed.
# At the end print all letters and the field.
# Input
# •	On the first line, you are given the initial string
# •	On the second line, you are given the integer N - the size of the square matrix
# •	The next N lines holds the values for every row
# •	On the next line you receive a number M
# •	On the next M lines you will get a move command
# Output
# •	On the first line the final state of the string
# •	In the end print the matrix
# Constraints
# •	The size of the square matrix will be between [2…10]
# •	The player position will be marked with "P"
# •	The letters on the field will be any letter except for "P"
# •	Move commands will be: "up", "down", "left", "right"


def entry_point(m):
    for r in range(len(m)):
        for c in range(len(m[r])):
            if m[r][c] == 'P':
                return r, c


def moving(m, place_to_move, r, c):
    if place_to_move == 'left':
        m, r, c = is_left(m, r, c)
    elif place_to_move == 'right':
        m, r, c = is_right(m, r, c)
    elif place_to_move == 'down':
        m, r, c = is_down(m, r, c)
    elif place_to_move == 'up':
        m, r, c = is_up(m, r, c)

    return m, r, c


def punishment():
    global word
    word = list(word)
    word.pop()
    return ''.join(word)


def is_left(m, r, c):
    if c == 0:
        punishment()
    else:
        m = move_player(m, r, c)
        c -= 1
        get_char(m, r, c)
        m[r][c] = 'P'

    return m, r, c


def is_down(m, r, c):
    if r == len(m) - 1:
        punishment()
    else:
        m = move_player(m, r, c)
        r += 1
        get_char(m, r, c)
        m[r][c] = 'P'

    return m, r, c


def is_up(m, r, c):
    if r == 0:
        punishment()
    else:
        m = move_player(m, r, c)
        r -= 1
        get_char(m, r, c)
        m[r][c] = 'P'

    return m, r, c


def is_right(m, r, c):
    if c == len(m[0]) - 1:
        punishment()
    else:
        m = move_player(m, r, c)
        c += 1
        get_char(m, r, c)
        m[r][c] = 'P'

    return m, r, c


def get_char(m, r, c):
    if m[r][c] != '-':
        global word
        word = list(word)
        word.append(m[r][c])
        m[r][c] = '-'
        return ''.join(word)


def move_player(m, r, c):
    m[r][c] = '-'
    return m


word = input()
matrix_range = int(input())
matrix = [list(input()) for c in range(matrix_range)]
movement_range = int(input())
start_row, start_col = list(map(int, entry_point(matrix)))
for _ in range(movement_range):
    move = input()
    matrix, start_row, start_col = moving(matrix, move, start_row, start_col)
print(''.join(word))
[print(''.join(c)) for c in matrix]
