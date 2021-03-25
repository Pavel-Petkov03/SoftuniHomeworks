# Hungry Hippos is a tabletop game made for 2–4 players,
# produced by Hasbro, under the brand of its subsidiary,
# Milton Bradley. The idea for the game was published in
# 1967 by toy inventor Fred Kroll and it was introduced in
# 1978. The objective of the game is for each player to collect
# as many marbles as possible with their 'hippo' (a toy hippo model).
# You will receive on the first line the rows of the matrix (n) and
# on the next n lines you will get each row of the matrix as a string
# (zeros and ones separated by a single space). You have to calculate how
# many blocks of food you have (connected ones horizontally or vertically)
# Example: Here you have 2 blocks of food
massive = []
n = int(input())
count = 0
value = 'x'
is_break = False
for c in range(n):
    a = input().split()
    massive.append(a)
index_row = 0
index_col = 0
is_found = False
while index_row < len(massive):
    while index_col < len(massive[index_row]):
        if index_row <= len(massive) - 1 and index_col <= len(massive[index_row])- 1:
            if int(massive[index_row][index_col]) == 1:
                massive[index_row][index_col] = 2
                is_found = True
                is_once = True
                if -len(massive[index_row]) <= index_col + 1 < len(massive[index_row]):
                    if int(massive[index_row][index_col + 1]) == 1 and is_once:
                        index_col += 1
                        is_once = False
                if -len(massive) <= index_row + 1 < len(massive)and is_once:
                    if int( massive[index_row + 1][index_col] ) == 1:
                        index_row += 1
                        is_once = False
                if -len(massive[index_row]) <= index_col - 1 < len(massive[index_row])and is_once:
                    if int( massive[index_row][index_col - 1] ) == 1:
                        index_col -= 1
                        is_once = False
                if -len(massive[index_row]) <= index_row - 1 < len(massive[index_row])and is_once:
                    if int( massive[index_row - 1][index_col] ) == 1:
                        index_row -= 1
                        is_once = False


            else:
                if is_found:
                    count += 1
                    index_row = 0
                    index_col = 0
                    is_found = False
                else:
                    index_col += 1
        else:
            if index_row <= len(massive) - 1:
                is_break = True
                break


    else:
        index_row += 1
        index_col = 0

print(count)










