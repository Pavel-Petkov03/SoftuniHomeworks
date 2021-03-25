# Задача 4. Туристически магазин
# Времето се затопля и туристи, започват да си правят разходки високо в планината,
# където все още сняг, като за целта те трябва да закупят нужната туристическа
# екипировка.
# Вашата задача е да напишете програма, която да изчислява,
# стойността на екипировката, както и дали определения бюджет е
# достатъчен или не, като се знае, че в магазина има следната промоция:
# Всеки трети продукт е на половин цена.
# Вход
# От конзолата се чете:
# •	На първи ред – бюджетът - реално число в интервала [1.00… 100000.00]
# •	След това поредица от два реда (до получаване на команда "Stop"
# или при заявка за купуване на продукт, чиято стойност е по-висока от
# наличния бюджет) :
# o	Име на продукта – текст
# o	Цена на продукта – реално число в интервала [1.00… 5000.00]
# Изход
# На конзолата да се отпечатат следните редове според случая:
# •	При получаване на командата "Stop", на един ред:
# o	"You bought {брой на закупените продукти} products for {цена на покупките} leva."
# •	При заявка за покупка на продукт, чиято цена е по-висока от останалите пари, на два реда:
# o	"You don't have enough money!"
# o	"You need {недостигащи пари} leva!"
budget = float(input())
command = input()
counter = 0
is_out_of_money = False
all_products = 0
price_for_product = 0
while command != "Stop":
    counter += 1
    product = command
    price_for_product = float(input())
    if counter % 3 == 0:
        price_for_product *= 0.5
    if price_for_product > budget:
        is_out_of_money = True
        break
    budget -= price_for_product
    all_products += price_for_product
    command = input()
if is_out_of_money:
    print("You don't have enough money!")
    print(f"You need {abs(budget - price_for_product):.2f} leva!")
else:
    print(f"You bought {counter} products for {all_products:.2f} leva.")

