# За великденските празници, магазин започва да продава три вида
# великденска украса – кошнички за яйца (basket), великденски венци (wreath)
# и шоколадови зайци (chocolate bunny). Вашата задача е да напишете програма,
# която да изчислява каква сметка трябва да плати всеки един клиент на магазина,
# като се има в предвид, че всеки клиент закупил четен брой продукти,
# ще получи 20% отстъпка от крайната цена. След като всички клиенти приключат
# с покупките, трябва да се отпечата средно по колко пари е похарчил всеки човек.
# Цените на продуктите са:
# •	кошничка за яйца (basket) – 1.50 лв.
# •	великденски венец (wreath) – 3.80 лв.
# •	шоколадов заек (chocolate bunny) – 7 лв.
# Вход
# От конзолата първоначално се чете един ред:
# •	Брои на клиентите в магазина – цяло число [1… 100]
# •	След това за всеки един клиент на нов ред до получаване на командата "Finish" се чете:
# o	Покупката която клиента е избрал – текст ("basket", "wreath" или "chocolate bunny")
# Изход
# •	При получаване на командата "Finish" да се отпечата един ред:
# o	"You purchased {броя на покупките} items for {крайната цена} leva."
# •	Накрая, след като всички клиенти приключат с покупките, да се отпечата на един ред
# o	"Average bill per client is: {средно аритметично на парите които е похарчил всеки един клиент} leva."
# Всички пари трябва да бъдат форматирани до втората цифра след десетичния знак.
count_of_clients = int(input())
all_money = 0
for c in range(1 , count_of_clients + 1):
    command = input()
    money_for_client = 0
    counter = 0
    while command != "Finish":
        counter += 1
        if command == "basket":
            money_for_client += 1.5
        elif command == "wreath":
            money_for_client += 3.8
        elif command == "chocolate bunny":
            money_for_client += 7
        command = input()
    if counter % 2 == 0:
        money_for_client *= 0.8
    print(f"You purchased {counter} items for {money_for_client:.2f} leva.")
    all_money += money_for_client
print(f"Average bill per client is: {(all_money / count_of_clients):.2f} leva.")