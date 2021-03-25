# You will be given a number n representing the number of rows of the field. On the next n lines you will receive each
# row of the field as a string with numbers separated by a space. Each number greater than zero represents a
# ship with a health equal to the number value. After that you will receive the squares that are being attacked
# in the format: "{row}-{col} {row}-{col}". Each time a square is being attacked, if there is a ship there
# (number greater than 0) you should reduce its value. After the attacks have ended, print how many ships were destroyed
# (if its value has reached zero)
massive = []
n = int(input())
counter =0
for times in range(n):
    new = []
    massive.append(input().split())
killing = input().split()
for kills in killing:
    row, col = kills.split("-")
    row = int(row)
    col = int(col)
    if int(massive[row][col]) == 0:
        pass
    else:
        value = int(massive[row][col])
        value -= 1
        massive[row][col] = value
        if int(massive[row][col]) == 0:
            counter += 1
print(counter)
