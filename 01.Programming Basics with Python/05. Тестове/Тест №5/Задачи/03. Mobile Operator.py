# Мобилен оператор предлага договори с различна месечна такса в
# зависимост от срока - 1 или 2 години.  Да се напише програма,
# която изчислява дължимата сума, която трябва да се плати за определен
# брой месеци.
# срок / тип	Small	Middle	Large	ExtraLarge
# 1 година(one)	9.98 лв.	18.99 лв.	25.98 лв.	35.99 лв.
# 2 години(two)	8.58 лв.	17.09 лв.	23.59 лв.	31.79 лв.
# Условия:
# •	при добавен мобилен интернет, към таксата за един месец се добавя:
# o	при такса по-малка или равна на 10.00 лв.  5.50 лв.
# o	при такса по-малка или равна на 30.00 лв.  4.35 лв.
# o	при такса по-голяма от 30.00 лв.  3.85 лв.
# •	ако договорът e за две години, общата сума се намалява с 3.75%
# Вход
# От конзолата се четат 3 реда:
# 1.	Срок на договор – текст – "one", или "two"
# 2.	Тип на договор – текст – "Small",  "Middle", "Large"или "ExtraLarge"
# 3.	Добавен мобилен интернет – текст – "yes" или "no"
# 4.	Брой месеци за плащане - цяло число в интервала [1 … 24]
# Изход
# На конзолата се отпечатва 1 ред:
# •	Цената, която заплаща клиентът,
# форматирана до втория знак след десетичната запетая, в следния формат:
# "{цената} lv."
session = input()
type_ = input()
mobile_internet = input()
months = int(input())
phone = 0
taxes_for_month = 0
if session == "one":
    if type_ == "Small":
        phone += 9.98
    elif type_ == "Middle":
        phone += 18.99
    elif type_ == "Large":
        phone += 25.98
    elif type_ == "ExtraLarge":
        phone += 35.99
elif session == "two":
    if type_ == "Small":
        phone += 8.58
    elif type_ == "Middle":
        phone += 17.09
    elif type_ == "Large":
        phone += 23.59
    elif type_ == "ExtraLarge":
        phone += 31.79
taxes_for_month += phone
if mobile_internet == "yes":
    if taxes_for_month <= 10:
        taxes_for_month += 5.50
    elif taxes_for_month <= 30:
        taxes_for_month += 4.35
    elif taxes_for_month > 30:
        taxes_for_month += 3.85
if session == "two":
    taxes_for_month *= 0.9625
print(f'{(taxes_for_month * months):.2f} lv.')
