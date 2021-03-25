# Задача 6. Любим филм
# Петък вечер е и се чудите кой филм да си пуснете да гледате. Решавате да напишете програма, която да избере това
# вместо вас. До команда "STOP" получавате заглавия на любими ваши филми. Най-добрият филм за вас ще бъде този, който
# има най-много точки. Точките се изчисляват като сбор от ASCII стойностите на символите в заглавието на филма.
# (няма да има случай, в който имаме два филма с равен брой точки)
# При изчислението на точките трябва да се има предвид следното:
# •	За всяка малка буква в заглавието, от сумата трябва да се извади два пъти дължината на заглавието на филма.
# •	За всяка главна буква в заглавието, от сумата трябва да се извади дължината на заглавието на филма.
# Може да имате максимум 7 заглавия на филми.
# Вход
# От конзолата се четат редове до команда "STOP" или до достигането на лимита от 7 филма:
# •	Заглавие на филм  – текст;
# Изход
# На конзолата да се отпечата:
# •	Ако сте достигнали лимита от 7 филма трябва да отпечатате:
# "The limit is reached."
# Да се отпечата най-добрият филм за вас:
# "The best movie for you is {заглавие на филм} with {сума на символите} ASCII sum."
import sys
command = input()
points = 0
all_points = 0
name = ''
max = -sys.maxsize
counter = 0
is_limit = False
while command != "STOP":
    counter += 1
    for symbol in command:
        symbol = ord(symbol)
        if 65 <= symbol <= 90:
            points = symbol - len(command)
        elif 97 <= symbol <= 122:
            points = symbol - 2 * len(command)
        else:
            points = symbol
        all_points += points
    if max < all_points:
        max = all_points
        all_points = 0
        name = command
    if counter == 7:
        is_limit = True
        break
    all_points = 0
    command = input()
if is_limit:
    print("The limit is reached.")
print(f"The best movie for you is {name} with {max} ASCII sum.")


