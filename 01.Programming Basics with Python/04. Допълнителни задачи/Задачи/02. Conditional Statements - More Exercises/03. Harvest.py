from math import floor
from math import ceil
# От лозе с площ X квадратни метри се заделя 40% от реколтата за производство на вино.
# От 1 кв.м лозе се изкарват Y килограма грозде. За 1 литър вино са нужни 2,5 кг. грозде. Желаното количество
# вино за продан е Z литра.
# Напишете програма, която пресмята колко вино може да се произведе и дали това количество е достатъчно.
# Ако е достатъчно, остатъкът се разделя по равно между работниците на лозето.
# Вход
# Входът се чете от конзолата и се състои от точно 4 реда:
# 1ви ред: X кв.м е лозето – цяло число в интервала [10 … 5000]
# 3ти ред: Z нужни литри вино – цяло число в интервала [10 … 600]
# 4ти ред: брой работници – цяло число в интервала [1 … 20]
land = int(input())
grapes = float(input()) * land
wine = (grapes / 2.5) * 0.4
needed_wine = int(input())
workers = int(input())
if wine >= needed_wine:
    left_wine = ceil((wine - needed_wine))
    wine_per_worker = ceil(((wine - needed_wine) / workers))
    print(f'Good harvest this year! Total wine: {floor(wine)} liters.')
    print(f'{ceil(left_wine)} liters left -> {ceil(wine_per_worker)} liters per person.')
else:
    not_enough_wine = (floor(needed_wine - wine))
    print(f'It will be a tough winter! More {abs(floor(not_enough_wine))} liters wine needed.')
