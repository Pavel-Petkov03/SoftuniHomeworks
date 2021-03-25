# Това е задача 1 от урок 2-Упражнение
# Басейн с обем V има две тръби от които се пълни.
# Всяка тръба има определен дебит (литрите вода минаващи през една тръба за един час).
# Работникът пуска тръбите едновременно и излиза за N часа. Напишете програма, която изкарва състоянието на басейна,
# в момента, когато работникът се върне.

v = int(input())  # Обем на басейн
p1 = int(input())  # Дебит на първа тръба
p2 = int(input())  # Дебит на втора тръба
n = float(input())  # Време на работа на тръбите
full = (p1 + p2) * n
percent_of_the_full = f'{full / v * 100:.2f}'
percent_of_p1 = f'{n * p1 / full * 100 :.2f}'
percent_of_p2 = f'{n * p2 / full * 100:.2f}'
difference = full - v
if v >= full:
    print(f'The pool is {percent_of_the_full}% full. Pipe 1: {percent_of_p1}%. Pipe 2: {percent_of_p2}%.')
else:
    print(f'For {n:.2f} hours the pool overflows with {difference:.2f} liters')
