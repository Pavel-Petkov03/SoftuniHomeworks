# We receive the size of the field in which our miner moves.
# The field is always a square. After that, we will receive the
# commands, which represent the directions, in which the miner should move.
# The miner starts from position - 's'. The commands will be: left, right, up and down.
# If the miner has reached the edge of the field and the next command indicates that he has
# to get out of the field, he must remain on his current possition and ignore the current command.
# The possible characters that may appear on the screen are:
# •	* - a regular position on the field.
# •	e - the end of the route.
# •	c  - coal
# •	s - the place where the miner starts
# When the miner finds a coal, he collects it and replaces it with '*'.
# Keep track of the count of the collected coals. If the miner collects all
# of the coals in the field, the program stops and you have to print the following message:
# "You collected all coals! ({rowIndex}, {colIndex})".
# If the miner steps at 'e', the game is over (the program stops) and you have to print the
# following message: "Game over! ({rowIndex}, {colIndex})".
# If there are no more commands and none of the above cases had happened, you have to print
# the following message: "{remainingCoals} coals left. ({rowIndex}, {colIndex})".
# Input
# •	Field size - an integer number.
# •	Commands to move the miner - an array of strings separated by " ".
# •	The field: some of the following characters (*, e, c, s), separated by whitespace (" ");
# Output
# •	There are three types of output:
# o	If all the coals have been collected, print the following output:
# "You collected all coals! ({rowIndex}, {colIndex})"
# o	If you have reached the end, you have to stop moving and print the
# following line: "Game over! ({rowIndex}, {colIndex})"
# o	If there are no more commands and none of the above cases had happened,
# you have to print the following message: "{totalCoals} coals left. ({rowIndex}, {colIndex})"
# Constraints
# •	The field size will be a 32-bit integer in the range [0 … 2 147 483 647].
# •	The field will always have only one 's'.
# •	Allowed working time for your program: 0.1 seconds.
# •	Allowed memory: 16 MB.


def is_in_boundary(row, col, m):
    if 0 <= row < len(m) and 0 <= col < len(m[0]):
        return True
    return False


def command_parsing(cmd, init_row, init_col, m):
    if cmd == 'right':
        init_col += 1
        if not is_in_boundary(init_row, init_col, m):
            init_col -= 1
    elif cmd == 'left':
        init_col -= 1
        if not is_in_boundary(init_row, init_col, m):
            init_col += 1
    elif cmd == 'up':
        init_row -= 1
        if not is_in_boundary(init_row, init_col, m):
            init_row += 1
    elif cmd == 'down':
        init_row += 1
        if not is_in_boundary(init_row, init_col, m):
            init_row -= 1

    return init_row, init_col


def entry_pos(m):
    for row in range(len(m)):
        for col in range(len(m[0])):
            if m[row][col] == 's':
                return row, col


def search(m):
    global counter_coal
    global max_coal
    new_row, new_col = entry_pos(m)
    for command in command_line:
        new_row, new_col = command_parsing(command, new_row, new_col, m)
        if m[new_row][new_col] == 'e':
            return f'Game over! ({new_row}, {new_col})'
        else:
            finding_symbol(new_row, new_col, m)
            if counter_coal == max_coal:
                return f'You collected all coals! ({new_row}, {new_col})'

    return f'{max_coal - counter_coal} coals left. ({new_row}, {new_col})'


def finding_symbol(r, c, m):
    if m[r][c] == 'c':
        global counter_coal
        counter_coal += 1
        m[r][c] = '*'


def all_coal_count(m):
    counter = 0
    for r in range(len(m)):
        for c in range(len(m[0])):
            if m[r][c] == 'c':
                counter += 1

    return counter


counter_coal = 0
initial_rows = int(input())
command_line = input().split()
matrix = [input().split() for c in range(initial_rows)]
max_coal = all_coal_count(matrix)
print(search(matrix))
