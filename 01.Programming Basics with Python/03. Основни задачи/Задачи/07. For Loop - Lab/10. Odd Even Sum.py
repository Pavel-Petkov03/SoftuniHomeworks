# Да се напише програма, която чете n-на брой цели числа, подадени от потребителя,
# и проверява дали сумата от числата на четни позиции е равна на сумата на числата на нечетни позиции.
# При равенство да се отпечатат два реда: "Yes" и на нов ред "Sum = " + сумата; иначе да се отпечата "No"
# и на нов ред "Diff = " + разликата.
# Разликата се изчислява по абсолютна стойност.
all_1 = 0
all_2 = 0
times = int(input())
for number in range(1, times + 1):
    value = int(input())
    if number % 2 == 0:
        all_1 += value
    elif number % 2 != 0:
        all_2 += value
if all_1 == all_2:
    print('Yes')
    print(f'Sum = {all_1}')
else:
    print('No')
    print(f'Diff = {abs(all_1 - all_2)}')




