#  Задача 6. Най-силната дума
#  За Лора думите притежават голяма сила. Тя те моли да измислиш алгоритъм, с който да откриеш коя е "най-силната" дума. До получаване на команда "End of words" ще се четат от конзолата думи. За да се открие силата на всяка една, трябва да се намери сборът от ASCII стойностите на символите, от които се състои думата. Ако започва с гласна буква - 'a', 'e', 'i', 'o', 'u', 'y' (или техните еквивалентни главни букви), полученият сбор трябва да се умножи по дължината на думата, в противен случай, да се раздели на дължината и да се закръгли до най-близкото цяло число надолу.
# Вход
# До получаване на команда "End of words" се чете по един ред от конзолата:
# •	дума – текст
# Изход
# След приключване на програмата се печата на един ред думата с "най-голяма сила":
# •	"The most powerful word is {думата с най-голяма сила} - {силата на думата}"
import sys
max_p = -sys.maxsize
points = 0
command = input()
best_word = ''
while command != "End of words":
    points = 0
    for letters in command:
        points += ord(letters)
    if command[0] == "a" or command[0] == "e" or  command[0] == "o" or command[0] == "i" or command[0] == "u" or \
            command[0] == "y" or command[0] == "A" or command[0] == "U" or command[0] == "I" or command[0] == "Y" or \
            command[0] == "O" or command[0] == "E":
        points *= len(command)
    else:
        points /= round(len(command))
    if points > max_p:
        max_p = points
        best_word = command
    command = input()
print(f"The most powerful word is {best_word} - {max_p}" )












