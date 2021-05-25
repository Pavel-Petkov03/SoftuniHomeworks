def create_matrix():
    return [[0 for _ in range(8)] for _ in range(6)]


def print_matrix(m):
    [print(index) for index in m]


def win_situation(m, special_number):
    if horizontal_checker(m, special_number) or vertical_checker(m, special_number) or down_up_diagonal_checker(m,
                                                                                                                special_number) \
            or up_down_diagonal_checker(m, special_number):
        return True
    return False


def fill_matrix(m, i, insert):
    for rev in reversed(range(len(m))):
        if m[rev][i] == 0:
            m[rev][i] = insert
            break
    return m


def validate_index(i, m):
    i -= 1
    if i in range(len(m[0])):
        return i
    return False


def horizontal_checker(m, special_number):
    for row in range(len(m)):
        helper = []
        for col in range(len(m[row]) - 3):
            helper.append(m[row][col])
        if helper.count(special_number) == 4:
            return True
    return False


def vertical_checker(m, special_number):
    for row in range(len(m) - 3):
        for col in range(len(m[row])):
            helper = []
            if m[row][col] != 0:
                helper.append(m[row][col])
                for add_row in range(1, 4):
                    helper.append(m[row + add_row][col])
                if helper.count(special_number) == 4:
                    return True
    return False


def up_down_diagonal_checker(m, special_number):
    for row in range(len(m) - 4, -1, -1):
        for col in range(len(m[row])):
            return common_diagonal_function(row, col, special_number, m)
    return False


def common_diagonal_function(row_, col_, special_number, m):
    helper = []
    row_template = [-1, -2, -3]
    col_template = [1, 2, 3]
    helper.append(m[row_][col_])
    for additional in range(3):
        initial_row = row_ + row_template[additional]
        initial_col = col_ + col_template[additional]
        helper.append(m[initial_row][initial_col])
    if len(helper) == 4 and helper.count(special_number) == 4:
        return True
    return False


def down_up_diagonal_checker(m, special_number):
    for row in range(len(m) - 1, len(m) - 4, -1):
        for col in range(len(m[row])):
            if m[row][col] != 0:
                return common_diagonal_function(row, col, special_number, m)
    return False


def play():
    matrix = create_matrix()
    player_state = 1
    next_player = 1
    print_matrix(matrix)
    while True:
        player_state = next_player
        initial_index = int(input(f'Player {player_state}, please choose a column:'))
        if player_state % 2 != 0:
            inserter = 1
            next_player = 2
        else:
            inserter = 2
            next_player = 1
        if validate_index(initial_index, matrix) is not bool:
            initial_index = validate_index(initial_index, matrix)
        else:
            continue
        matrix = fill_matrix(matrix, initial_index, inserter)

        if win_situation(matrix, inserter):
            print_matrix(matrix)
            print(f'Player {player_state} you win')
            break
        print_matrix(matrix)


play()