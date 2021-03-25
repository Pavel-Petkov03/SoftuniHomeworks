# Напишете програма, която чете цяло число n, въведено от потребителя, и отпечатва пирамида от числа като в примерите:
n = int(input())
number = 0
is_bigger = False
for rows in range(1 , n + 1):
    for columns in range(1 , rows + 1):
        number += 1
        if number > n:
            is_bigger = True
            break
        print(str(number) + ' ', end='' )
    if is_bigger:
        break
    print()