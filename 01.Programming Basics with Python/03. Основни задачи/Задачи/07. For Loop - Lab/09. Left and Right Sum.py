# Да се напише програма, която чете 2*n-на брой цели числа, подадени от потребителя,
# и проверява дали сумата на първите n числа (лява сума) е равна на сумата на вторите n числа (дясна сума).
# При равенство печата " Yes, sum = " + сумата; иначе печата " No, diff = " + разликата.
# Разликата се изчислява като положително число (по абсолютна стойност).




n = int(input())
sum_first = 0
sum_second = 0

for number in range(1 , n + 1):
    value = int(input())
    sum_first += value
for number in range(1, n + 1):
    value = int(input())
    sum_second += value
if sum_first == sum_second:
    print(f'Yes, sum = {sum_second}')
elif sum_first != sum_second:
    dif = abs(sum_second - sum_first)
    print(f'No, diff = {dif}')
