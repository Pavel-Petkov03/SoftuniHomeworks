# Задача 5. Сериали
# От телевизионна компания ви наемат да създадете програма, която да изчислява дали за клиентите ще е възможно да си закупят желаните сериали. Разполагате с бюджет и брой сериали, които потребителят ще желае да закупи. Всеки сериал съответно има заглавие и цена.
# Някои от сериалите имат намаление:
# •	Thrones – 50%
# •	Lucifer – 40%
# •	Protector – 30%
# •	TotalDrama – 20%
# •	Area – 10%
# Вход
# От конзолата се четат:
# •	Бюджет  - реално  число в интервала [10.0… 100.0]
# •	Брой сериали - n - цяло положително число в интервала [1… 10]
# За всеки сериал се четат по два реда:
# o	Име на сериал - текст
# o	Цена за сериал -  реално  число в интервала [1.0… 15.0]
# Изход
# На конзолата да се изпише един ред:
# •	Ако бюджета ви е по-голям или равен на цената на сериалите:
# 	"You bought all the series and left with {останали пари} lv."
# •	Ако бюджета ви е по-малък от цената на сериалите:
# 	"You need {нужни пари} lv. more to buy the series!"
# Резултатът да бъде закръглен до втората цифра след десетичния знак.
budget = float(input())
series = int(input())
all_money = 0
is_left = False
for c in range(1 , series + 1):
    series_name = input()
    price_for_series = float(input())
    if series_name == 'Thrones':
        price_for_series *= 0.5
    elif series_name == "Lucifer":
        price_for_series *= 0.6
    elif series_name == "Protector":
        price_for_series *= 0.7
    elif series_name == "TotalDrama":
        price_for_series *= 0.8
    elif series_name == "Area":
        price_for_series *= 0.9
    if budget < all_money:
        is_left = True
    all_money += price_for_series
if is_left:
    print(f"You need {abs(budget - all_money):.2f} lv. more to buy the series!" )
else:
    print(f"You bought all the series and left with {abs(all_money - budget):.2f} lv.")
