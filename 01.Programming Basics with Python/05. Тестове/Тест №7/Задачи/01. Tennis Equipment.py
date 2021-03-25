# Задача 1. Оборудване за тенис
# Световният номер едно в мъжкия тенис Новак Джокович е решил да подмени оборудването, с което играе своите мачове.
# За целта той ви моли да напишете програма, която да изчисли стойността на покупките,
# като се има предвид, че той трябва да заплати 1/8 от цената, а останалите 7/8 трябва да бъдат заплатени
# от неговите спонсори.
# Джокович иска да закупи n на брой тенис ракети и m чифта маратонки, както и друга екипировка, на стойност 20%
# от общата цена на закупените ракети и маратонки.
# Известно е, че:
# •	1 чифт маратонки = 1/6 от цената на една тенис ракета
# Вход
# От конзолата се прочитат 3 реда:
# •	Цена на една тенис ракета – реално число в интервала [0.00…100000.00]
# •	Брой тенис ракети - цяло число в интервала [0…100]
# •	Брой чифтове маратонки - цяло число в интервала [0…100]
# Крайната цена се сформира от сумата от цената на ракетите, цената на маратонките и цената на останалата екипировка.
# Изход
# На конзолата се отпечатват 2 реда:
# •	"Price to be paid by Djokovic {1/8 от общата цена, закръглена към по-малкото цяло число}"
# •	"Price to be paid by sponsors {7/8 от общата цена, закръглена към по-голямото цяло число}"
import math
price_for_rocket = float(input())
number_of_rocket = int(input())
number_of_sneakers = int(input())
price_for_sneakers = price_for_rocket / 6
all_sneakers = price_for_sneakers * number_of_sneakers
all_price = (price_for_sneakers * number_of_sneakers + price_for_rocket * number_of_rocket) * 0.2
final_price = number_of_rocket * price_for_rocket + all_price + all_sneakers
Djokovich_pay = final_price / 8
sponsors_price = final_price - Djokovich_pay
print(f"Price to be paid by Djokovic {math.floor(Djokovich_pay)}")
print(f"Price to be paid by sponsors {math.ceil(sponsors_price)}")