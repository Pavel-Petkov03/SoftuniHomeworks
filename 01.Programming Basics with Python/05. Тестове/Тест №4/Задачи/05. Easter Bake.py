from math import ceil
import sys
# Задача 5. Великденски козунаци
# Предстои Великден и Деси е решила да изпече домашни козунаци за колегите си.
# Главните продукти, които ще трябват на Деси са: брашно и захар.
# Един пакет захар е 950 грама, а един пакет брашно е 750 грама.
# Напишете програма, която изчислява колко пакета захар и брашно
# трябва да купи Деси, за да й стигнат за направата на козунаците,
# като знаете за всеки един козунак по колко грама захар и брашно са
# изразходени. Също намерете кое е най-голямото количество захар и брашно,
# които са използвани.
# Вход
# От конзолата се чете 1 ред:
# •	 Броят на козунаците – цяло число в интервала [1 ... 100]
# За всеки козунак се чете:
# o	Количество изразходвана захар (грамове) – цяло число в интервала [1 … 10000]
# o	Количество изразходвано брашно (грамове) – цяло число в интервала [1 … 10000]
# Изход
# Да се отпечатат на конзолата 3 реда:
# •	"Sugar: {брой нужни пакети захар}"
# •	"Flour: {брой нужни пакет брашно}"
# •	"Max used flour is {максимално количество грамове брашно,
# използвани за правенето на козунак} grams, max used sugar is
# {максимално количество грамове захар, използвани за правенето на козунак} grams."
# Пакетите захар и брашно да бъдат закръглени към най-близкото цяло число нагоре.
easter_breads = int(input())
max_sugar = -sys.maxsize
max_flour = -sys.maxsize
all_sugar = 0
all_flour = 0
for c in range(1 , easter_breads +1 ):
    sugar = int(input())
    flour = int(input())
    if max_sugar < sugar:
        max_sugar = sugar
    if max_flour < flour:
        max_flour = flour
    all_sugar += sugar
    all_flour += flour
packets_of_sugar = ceil(all_sugar / 950)
packets_of_flour = ceil(all_flour / 750)

print(f"Sugar: {packets_of_sugar}")
print(f"Flour: {packets_of_flour}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")
