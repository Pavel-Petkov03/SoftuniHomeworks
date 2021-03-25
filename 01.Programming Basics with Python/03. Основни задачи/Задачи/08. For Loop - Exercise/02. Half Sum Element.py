import sys
# Да се напише програма, която чете n-на брой цели числа, въведени от потребителя,
# и проверява дали сред тях съществува число, което е равно на сумата на всички останали.
# Ако има такъв елемент, печата "Yes", "Sum = "  + неговата стойност; иначе печата "No", "Diff = " +
# разликата между най-големия елемент и сумата на останалите
# (по абсолютна стойност).
count = int(input())
max = -sys.maxsize
sum_all = int()
n = int()
for number in range(1 , count + 1):
    n = int(input())
    if n > max:
        max = n
    sum_all += max
if max == sum_all:
    print("Yes")
    print(f"Sum = {sum_all}")
else:
    print("No")
    print(f"Diff = {abs(max - sum_all)}")
