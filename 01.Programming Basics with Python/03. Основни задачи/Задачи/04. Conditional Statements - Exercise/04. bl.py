# Да се напише програма, която преобразува разстояние между следните 3 мерни единици: mm, cm, m.
# Използвайте съответствията от таблицата по-долу:
# входна единица	изходна единица
# 1 meter (m)	1000 millimeters (mm)
# 1 meter (m)	100 centimeters (cm)
# Входните данни се състоят от три реда, въведени от потребителя:
# 	Първи ред: число за преобразуване - реално число;
# 	Втори ред: входна мерна единица – текст;
# 	Трети ред: изходна мерна единица (за резултата) – текст.
# На конзолата да се отпечата резултатът от преобразуването на мерните единици,
# форматиран до третия знак след десетичната запетая.
number = float(input())
in_currency = input()
out_currency = input()
result = 0
if in_currency == 'mm':
    if out_currency == "cm":
        result = number / 10
    elif out_currency == "m":
        result = number / 1000
elif in_currency == "cm":
    if out_currency == "m":
        result = number / 100
    elif out_currency == "mm":
        result = number * 10
elif in_currency == 'm':
    if out_currency == "cm":
        result = number * 100
    elif out_currency == "mm":
        result = number * 1000
print(f'{result:.3f}')
