# You will be given a chess board (8x8). On the board there will be 3 types of symbols:
# •	"." – empty square
# •	"Q" – a queen
# •	"K" – the king
# Your job is to find which queens can capture the king and print them. The moves that the queen can do is to
# move diagonally, horizontally and vertically (basically all the moves that all the other figures can
# do except from the knight). Beware that there might be queens that stand in the way of other queens
# and can stop them from capturing the king. For more clarification see the examples.
# Input
# •	8 lines – the state of the board (each square separated by single space)
# Output
# •	The positions of the queens that can capture the king as lists
# •	If the king cannot be captured, print: "The king is safe!"
# •	The order of output does not matter
# Constrains
# •	There will always be exactly 8 lines
# •	There will always be exactly one King
# •	Only the 3 symbols described above will be present in the input


board_length = 8
final_list = []
matrix = [input().split() for c in range(board_length)]


def is_another_queen(m,r,c):
    if m[r][c] == 'Q':
        return True
    return False


def see_queen(m, r, c):
    if horizontal_logic(m, r, c) or vertical_logic(m, r, c) or diagonal_logic(m, r, c):
        global final_list
        final_list.append([r, c])


def horizontal_logic(m, r, c):
    for left_check in range(1, c+1):
        if not is_another_queen(m, r, c - left_check):
            if check_for_validation(m, r, c - left_check):
                return True
        else:
            break
    for right_check in range(1, len(m[r]) - c):
        if not is_another_queen(m, r, c+right_check):
            if check_for_validation(m, r, c+right_check):
                return True
        else:
            break
    return False


def vertical_logic(m, r, c):
    for up_check in range(1, r+1):
        if not is_another_queen(m, r-up_check, c):
            if check_for_validation(m, r-up_check, c):
                return True
        else:
            break
    for down_check in range(1, len(m) - r):
        if not is_another_queen(m, r+down_check, c):
            if check_for_validation(m, r+down_check, c):
                return True
        else:
            break
    return False


def diagonal_logic(m, r, c):
    for up_left in range(1, r + 1):
        if check_for_range(m, r - up_left, c - up_left):
            if not is_another_queen(m, r - up_left, c - up_left):
                if check_for_validation(m, r - up_left, c - up_left):
                    return True
            else:
                break
    for up_right in range(1, r + 1):
        if check_for_range(m, r - up_right, c + up_right):
            if not is_another_queen(m, r - up_right, c + up_right):
                if check_for_validation(m, r - up_right, c + up_right):
                    return True
            else:
                break

    for down_left in range(1,len(m) - r+1):
        if check_for_range(m, r + down_left, c - down_left):
            if not is_another_queen(m, r + down_left, c - down_left):
                if check_for_validation(m, r + down_left, c - down_left):
                    return True
            else:
                break
    for down_right in range(1,len(m) - r+1):
        if check_for_range(m, r + down_right, c + down_right):
            if not is_another_queen(m, r + down_right, c + down_right):
                if check_for_validation(m, r + down_right, c + down_right):
                    return True
            else:
                break
    return False


def check_for_validation(m, r, c):
    if r not in range(len(m)) or c not in range(len(m[0])):
        return False
    elif m[r][c] == 'K':
        return True
    return False


def check_for_range(m, r, c):
    if r in range(len(m)) and c in range(len(m[r])):
        return True
    return False


for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == 'Q':
            see_queen(matrix, row, col)


if not final_list:
    print('The king is safe!')
else:
    [print(c) for c in final_list]

