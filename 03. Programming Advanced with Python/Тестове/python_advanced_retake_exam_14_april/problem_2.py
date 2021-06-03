won = False
import re
first_player, second_player = input().split(', ')
matrix = []
for _ in range(7):
    matrix.append(input().split(' '))

dect = {
    first_player: [501, 0],
    second_player: [501, 0]
}
person = second_player
while dect[first_player][0] > 0 and dect[second_player][0] > 0:
    row, col = list(map(int, re.findall('\d+' ,input())))
    if row in range(len(matrix)) and col in range(len(matrix[0])):
        if person == first_player:
            person = second_player
        else:
            person = first_player
        dect[person][1] += 1
        if matrix[row][col] == 'D':
            dect[person][0] -= (int(matrix[row][0]) + int(matrix[row][-1]) + int(matrix[-1][col]) + int(
                matrix[0][col])) * 2
        elif matrix[row][col] == 'T':
            dect[person][0] -= (int(matrix[row][0]) + int(matrix[row][-1]) + int(matrix[-1][col]) + int(
                matrix[0][col])) * 3
        elif matrix[row][col] == 'B':

            print(f'{person} won the game with {dect[person][1]} throws!')
            won = True
            break
        else:
            dect[person][0] -= int(matrix[row][col])
            dect[person][1] += 1
    else:
        if person == first_player:
            person = second_player
        else:
            person = first_player
        dect[person][1] += 1

if not won:
    print(f'{person} won the game with {dect[person][1]} throws!')
