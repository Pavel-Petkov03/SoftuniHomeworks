
from math import floor
# Фирма получава заявка за изработването на проект, за който са необходими определен брой часове.
# Фирмата разполага с определен брой дни. През 10% от дните служителите са на обучение и не могат да работят по проекта.
# Един нормален работен ден във фирмата е 8 часа.
# Всеки служител може да работи по проекта в извънработно време по 2 часа на ден.
# Часовете трябва да са закръглени към по-ниско цяло число (Например –> 6.98 часа се закръглят на 6 часа).
# Напишете програма, която изчислява дали фирмата може да завърши проекта навреме и колко часа не достигат или остават.

hours = int(input())
days = int(input())
out_hour_workers = int(input())
days_left = days - 0.1 * days
full = floor(days_left * 8 + out_hour_workers * 2 * days)
if hours <= full:
    left_time = hours - full
    print(f'Yes!{abs(left_time)} hours left.')
else:
    not_enough_time = full - hours
    print(f'Not enough time!{abs(not_enough_time)} hours needed.')





