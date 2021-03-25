# Напишете програма която пресмята колко пари ще изкара шофьор на ТИР за един сезон.
# На входа програмата получава през кой сезон ще работи шофьора, както и колко километра на месец ще кара.
# Един сезон е 4 месеца. Според зависи сезона и броя километри на месец ще му се заплаща различна сума на километър:
#
# 	Пролет/Есен	Лято	Зима
# км на месец <= 5000	0.75 лв./км	0.90 лв./км	1.05 лв./км
# 5000 < км на месец <= 10000	0.95 лв./км	1.10 лв./км	1.25 лв./км
# 10000 < км на месец <= 20000	1.45 лв./км – за който и да е сезон
#
# След като са извадени 10% за данъци се отпечатват останалите пари.
# Вход
# Входът се чете от конзолата и се състои от два реда:
# •	Първи ред – Сезон – текст "Spring", "Summer", "Autumn" или "Winter"
# •	Втори ред –  Километри на месец – реално число в интервала [10.00...20000.00]
# Изход
# На конзолата трябва да се отпечатат едно число:
# •	Заплатата на шофьора след данъците, форматирана до втория знак след десетичната запетая.
season = input()
kilometers_per_month = float(input())
months = 4
price = float()
if kilometers_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        price = months * kilometers_per_month * 0.75
    elif season == "Summer":
        price = months * kilometers_per_month * 0.90
    elif season == "Winter":
        price = months * kilometers_per_month * 1.05
elif 5000 < kilometers_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        price = months * kilometers_per_month * 0.95
    elif season == "Summer":
        price = months * kilometers_per_month * 1.10
    elif season == "Winter":
        price = months * kilometers_per_month * 1.25
elif 10000 < kilometers_per_month <= 20000:
    price = months * kilometers_per_month * 1.45
price *= 0.9
print(f'{price:.2f}')







