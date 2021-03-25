# Задача 6. Игра на имена
# Иван е измислил нова игра в която да се състезава със своите приятели. Вашата задача е да напишете програма за играта. Всеки играч написва името си, след това за всяка една буква от името си написва по едно цяло число, ако числото съвпада с ASCII стойността на съответната буква, играчът получава 10 точки, в противен случай, получава само 2 точки. Победител е играчът с най-много точки в края на играта. В случай, че двама играчи имат равен брой точки, печели този, който втори е достигнал резултата.
# Вход
# До получаване на командата "Stop" се чете по един ред:
# •	Име на играча с дължина n - текст
# За всеки играч се четат n на брой реда:
# •	число – цяло число в интервала[0…127]
# Изход
# Да се отпечата един ред в следния формат:
# •	"The winner is {името на победителя} with {точките на победителя} points!"
import sys
command = input()
max_p = -sys.maxsize
winner = ''
while command != "Stop":
    all_points = 0
    for letters in command:
        points = 0
        number = int(input())
        if ord(letters) == number:
            points += 10
        else:
            points += 2
        all_points += points
    if all_points >= max_p:
        max_p = all_points
        winner = command
    command = input()
print(f"The winner is {winner} with {max_p} points!")
