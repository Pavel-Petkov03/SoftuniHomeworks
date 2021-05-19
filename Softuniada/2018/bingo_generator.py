number = input()
first_num = f'{number[0]}{number[2]}'
second_num = f'{number[1]}{number[3]}'
roof = int(first_num) + int(second_num)
start_element = first_num + second_num
twelves = []
fifteens = []
for number in range(int(start_element), 10000):
    if int(str(number)[0:2]) <= roof and int(str(number)[2:]) <= roof and int(str(number)[2:]) >= int(str(start_element)[2:]):
        if number % 12 == 0:
            twelves.append(number)
        if number % 15 == 0:
            fifteens.append(number)

print(f'Dividing on 12: {" ".join([str(c) for c in twelves])}')
print(f'Dividing on 15: {" ".join([str(c) for c in fifteens])}')
print('!!!BINGO!!!'if len(fifteens) == len(twelves) else 'NO BINGO!')


