# Hungry Hippos is a tabletop game made for 2–4 players, produced by Hasbro, under the brand of its subsidiary,
# Milton Bradley. The idea for the game was published in 1967 by toy inventor Fred Kroll and it was introduced in 1978.
# The objective of the game is for each player to collect as many marbles as possible with their 'hippo'
# (a toy hippo model).
# You will receive on the first line the rows of the matrix (n) and on the next n lines you will get each row of the
# matrix as a string (zeros and ones separated by a single space). You have to calculate how many blocks of food you
# have (connected ones horizontally or diagonally)
# Example: Here you have 2 blocks of food


matrix = [input().split() for index in range(int(input()))]

def recursion(start_r, count_, matrix_):
    is_bad = False
    for row in range(start_r, len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == '1':
                if row in range(len(matrix) - 1) and col in range(len(matrix[row]) - 1) and matrix[row][col+1] == '1' \
                        and matrix[row + 1][col] == '1':
                    is_bad = True
                if row in range(len(matrix) - 1) and matrix[row+1][col] == '1':
                    matrix[row][col] = 0
                elif col in range(len(matrix[row]) - 1) and matrix[row][col+1] == '1':
                    matrix[row][col] = 0
                else:
                    if is_bad:
                        pass
                    else:
                        if row in range(len(matrix) - 1) and matrix[row-1][col] == '1':
                            pass
                        else:
                            count_ += 1
        is_bad = False
        start_r += 1
        return recursion(start_r, count_, matrix_)
    return count_


print(recursion(0, 0, matrix))



