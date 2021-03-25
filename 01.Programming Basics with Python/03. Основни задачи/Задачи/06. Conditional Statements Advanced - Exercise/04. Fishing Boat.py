# Тони и приятели много обичат да ходят за риба и са толкова запалени по риболова,
# че решават да отидат на риболов с кораб.
# Цената за наема на кораба зависи от сезона и броя рибари:
# В зависимост от сезона:
# •	Цената за наем на кораба през пролетта е  3000 лв.;
# •	Цената за наем на кораба през лятото и есента е  4200 лв.;
# •	Цената за наем на кораба през зимата е  2600 лв.
# В зависимост от броя на групата има различна отстъпка:
# •	Ако групата е до 6 човека включително  –  отстъпка от 10%;
# •	Ако групата е от 7 до 11 човека включително  –  отстъпка от 15%;
# •	Ако групата е от 12 нагоре  –  отстъпка от 25%.
# Рибарите ползват допълнително 5% отстъпка, ако са четен брой, освен ако не е есен -
# тогава нямат допълнителна отстъпка, която се начислява след като се приспадне отстъпката по горните критерии.
# Напишете програма, която да пресмята дали рибарите ще съберат достатъчно пари.
# Вход
# От конзолата се четат три реда:
# •	Бюджет на групата – цяло число;
# •	Сезон –  текст: "Spring", "Summer", "Autumn" или "Winter";
# •	Брой рибари – цяло число.
# Изход
# На конзолата да се отпечата следното:
# •	Ако бюджетът е достатъчен:
# "Yes! You have {останалите пари} leva left."
# •	Ако бюджетът НЕ Е достатъчен:
# "Not enough money! You need {сумата, която не достига} leva."
# Сумите трябва да са форматирани с точност до два знака след десетичната запетая.
budget = int(input())
season = input()
fishers = int(input())
price = float()
if season == "Spring":
    price = 3000
    if fishers <= 6:
        price = price - price * 0.1
    elif 7 < fishers <= 11:
        price = price - 0.15 * price
    elif fishers > 12:
        price = price - price * 0.25
    if fishers % 2 == 0:
        price = price - price * 0.05
elif season == "Summer":
    price = 4200
    if fishers <= 6:
        price = price - price * 0.1
    elif 7 < fishers <= 11:
        price = price - 0.15 * price
    elif fishers > 12:
        price = price - price * 0.25
    if fishers % 2 == 0:
        price = price - price * 0.05
elif season == "Autumn":
    price = 4200
    if fishers <= 6:
        price = price - price * 0.1
    elif 7 < fishers <= 11:
        price = price - 0.15 * price
    elif fishers > 12:
        price = price - price * 0.25
elif season == "Winter":
    price = 2600
    if fishers <= 6:
        price = price - price * 0.1
    elif 7 < fishers <= 11:
        price = price - 0.15 * price
    elif fishers > 12:
        price = price - price * 0.25
    if fishers % 2 == 0:
        price = price - price * 0.05
if budget >= price:
    print(f"Yes! You have {(budget - price):.2f} leva left.")
else:
    print(f"Not enough money! You need {(price - budget):.2f} leva.")
