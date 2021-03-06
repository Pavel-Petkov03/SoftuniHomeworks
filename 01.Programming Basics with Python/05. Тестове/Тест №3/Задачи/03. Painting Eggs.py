# С наближаването на Великденските празници, цех за боядисване на яйца,
# започва да боядисва различни размери яйца, които след това продава на партиди.
# В таблицата са показани размерите на яйцата, различните бои и каква е цената за
# продажба на една партида яйца, зависеща от размерите и цвета боя.
# 	Червено (Red)	Зелено (Green)	Жълто (Yellow)
# Големи (Large)	16 лв.	12 лв.	9 лв.
# Средни (Medium)	13 лв.	9 лв.	7 лв.
# Малки (Small)	9 лв.	8 лв.	5 лв.
# Напишете програма, която изчислява какви ще са приходите на цеха от продажбите,
# като знаете размера на яйцата и техният цвят. С 35% от крайната цена ще бъдат
# покрити производствени разходи.
# Вход
# Входът се чете от конзолата и се състои от три реда:
# •	Първи ред – размер на яйцата – текст с възможности "Large", "Medium" или "Small"
# •	Втори ред – цвят на яйцата – текст  с възможности "Red", "Green" или "Yellow"
# •	Трети ред – брой партиди – цяло число в интервала [1… 350]
# Изход
# На конзолата трябва да се отпечата един ред:
# "{крайната цена} leva."
# Резултатът да се форматира до втората цифра след десетичния знак.
size = input()
color = input()
quantity = int(input())
price_for_egg = 0
if size == "Large":
    if color == "Red":
        price_for_egg = 16
    elif color == "Green":
        price_for_egg = 12
    elif color == "Yellow":
        price_for_egg = 9
elif size == "Medium":
    if color == "Red":
        price_for_egg = 13
    elif color == "Green":
        price_for_egg = 9
    elif color == "Yellow":
        price_for_egg = 7
elif size == "Small":
    if color == "Red":
        price_for_egg = 9
    elif color == "Green":
        price_for_egg = 8
    elif color == "Yellow":
        price_for_egg = 5
all_price = (price_for_egg * quantity) * 0.65
print(f"{all_price:.2f} leva.")
