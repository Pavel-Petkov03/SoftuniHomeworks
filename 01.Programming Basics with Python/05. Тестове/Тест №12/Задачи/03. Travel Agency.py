# Туристическа агенция има нужда от система за изчисляване на дължимата сума при резервация. В зависимост от различните дестинации и различните пакети, цената е различна.
# Цените за ден са следните:
# Цена за ден	Банско/Боровец	Варна/Бургас
# 	с екипировка	без екипировка	със закуска	без закуска
# 	100лв.	80лв	130лв.	100лв.
# VIP отстъпка	10%	5%	12%	7%
# Ако клиентът е заявил престой повече от 7 дни, получава единия ден безплатно.
# Вход
# От конзолата се четат 4 реда:
# 1.	Име на града - текст с възможности ("Bansko",  "Borovets", "Varna" или "Burgas")
# 2.	Вид на пакета - текст с възможности ("noEquipment",  "withEquipment", "noBreakfast" или "withBreakfast")
# 3.	Притежание на VIP отстъпка - текст с възможности  "yes" или "no"
# 4.	Дни за престой - цяло число в интервала [1 … 10000]
# Изход
# На конзолата се отпечатва 1 ред:
# •	Когато потребителят е въвел всички данни правилно, отпечатваме:
# "The price is {цената, форматирана до втория знак}lv! Have a nice time!"
# •	Ако потребителят е въвел по-малко от 1 ден за престой, отпечатваме:
# "Days must be positive number!"
# •	Когато при въвеждането на града или вида на пакета се въведат невалидни данни, отпечатваме: "Invalid input!"
city = input()
package = input()
vip_discount = input()
days = int(input())
price = 0
discount = 0
if package == "withEquipment":
    price = 100
    discount = 10
elif package == "noEquipment":
    price = 80
    discount = 5
elif package == "withBreakfast":
    price = 130
    discount = 12
elif package == "noBreakfast":
    price = 100
    discount = 7
if days > 7:
    days -= 1
if vip_discount == "yes":
    all_price = (price - price * discount / 100) * days
else:
    all_price = price * days
if days <= 0:
    print("Days must be positive number!")
elif (city == "Bansko" or city == "Borovets" or city == "Varna" or city == "Burgas") and (package ==
    "withEquipment" or package == "noEquipment"  or package == "noBreakfast" or package == "withBreakfast"):
    print( f"The price is {all_price:.2f}lv! Have a nice time!" )
else:
    print( "Invalid input!" )

