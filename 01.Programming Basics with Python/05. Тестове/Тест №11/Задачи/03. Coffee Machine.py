# Напишете софтуер, който да пресмята сметката на клиент, закупил определен брой от дадена напитка от кафемашина.
# 	Без захар	Нормално	Допълнително захар
# Еспресо	0.90 лв./бр.	1 лв. /бр.	1.20 лв. /бр.
# Капучино	1.00 лв. /бр.	1.20 лв. /бр.	1.60 лв. /бр.
# Чай	0.50 лв. /бр.	0.60 лв. /бр.	0.70 лв. /бр.
# Трябва да имате предвид следните отстъпки:
# •	При избрана напитка без захар има 35% отстъпка.
# •	При избрана напитка "Espresso" и закупени поне 5 броя, има 25% отстъпка.
# •	При сума надвишава 15 лева, 20% отстъпка от крайната цена,
# Отстъпките се прилагат в реда на тяхното описване.
# Вход
# Входът се чете от конзолата и се състои от три реда:
# •	Първи ред - напитка - текст с възможности"Espresso", "Cappuccino" или "Tea"
# •	Втори ред - захар - текст  с възможности "Without", "Normal" или "Extra"
# •	Трети ред - брой напитки - цяло число в интервала [1… 50]
# Изход
# На конзолата трябва да се отпечата един ред:
# "You bought {брой напитки} cups of {напитка} for {крайна цена} lv."
# Цената да бъде форматирана до втората цифра след десетичния знак.
drink = input()
sugar = input()
count = int(input())
price = 0
if drink == "Espresso":
    if sugar == "Without":
        price += 0.9
    elif sugar == "Normal":
        price += 1
    elif sugar == "Extra":
        price += 1.2
elif drink == "Cappuccino":
    if sugar == "Without":
        price += 1
    elif sugar == "Normal":
        price += 1.2
    elif sugar == "Extra":
        price += 1.6
elif drink == "Tea":
    if sugar == "Without":
        price += 0.5
    elif sugar == "Normal":
        price += 0.6
    elif sugar == "Extra":
        price += 0.7
all_price = price * count
if sugar == "Without":
    all_price *= 0.65
if drink == "Espresso" and count >= 5:
    all_price *= 0.75
if all_price > 15:
    all_price *= 0.8
print(f"You bought {count} cups of {drink} for {all_price:.2f} lv.")


