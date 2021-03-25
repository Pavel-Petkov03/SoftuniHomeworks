import sys
# Напишете програма, която чете n на брой цели числа.
# Принтирайте най-голямото и най-малкото число сред въведените.
n = int(input())
max = -sys.maxsize
min = sys.maxsize
for number in range(1 , n + 1):
    value = int(input())
    if value > max:
        max = value
    if value < min:
        min = value
print(f'Max number: {max}')
print(f'Min number: {min}')