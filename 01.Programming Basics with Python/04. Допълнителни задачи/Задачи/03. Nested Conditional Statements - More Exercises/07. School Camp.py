# Частно училище организира лагери за учениците по време на ваканциите.
# В зависимост от вида на ваканцията (пролетна, лятна или зимна) и вида на групата
# (момчета/момичета или смесена) цената на нощувката в хотела е различна, както и спортът,
# който ще практикуват учениците.
# 	Зимна ваканция	Пролетна ваканция	Лятна ваканция
# момчета/момичета	9.60	7.20	15
# смесена група	10	9.50	20
# Училището получава отстъпка от крайната цена, в зависимост от броя на настанените в хотела ученици:
# •	Ако броят на учениците е 50 или повече, училището получава 50% отстъпка
# •	Ако броят на учениците е 20 или повече и в същото време по-малък от 50, училището получава 15% отстъпка
# •	Ако броят на учениците е 10 или повече и в същото време по-малък от 20, училището получава 5% отстъпка
# В таблицата по-долу са дадени спортовете, които ще се практикуват в зависимост от вида на ваканцията и групата:
# 	Зимна ваканция	Пролетна ваканция	Лятна ваканция
# момичета	Gymnastics	Athletics	Volleyball
# момчета	Judo	Tennis	Football
# смесена група	Ski	Cycling	Swimming
# Да се напише програма, която пресмята цената, която ще заплати училището за нощувките и принтира спорта,
# който ще се практикува от учениците.
# Вход
# От конзолата се четат 4 реда:
# 1.	Сезонът – текст - “Winter”, “Spring” или “Summer”;
# 2.	Видът на групата – текст - “boys”, “girls” или “mixed”;
# 3.	Брой на учениците – цяло число в интервала [1 … 10000];
# Брой на нощувките – цяло число в интервала [1 … 100].
# Изход
# На конзолата се отпечатва 1 ред:
# •	Спортът, който са практикували учениците и цената за нощувките, която е заплатило училището,
# форматирана до втория знак след десетичната запетая, в следния формат:
# "{спортът} {цената} lv.“
season = input()
group = input()
people = int(input())
night = int(input())
sport = ''
price = float()
if season == 'Winter':
    if group == "boys" or group == "girls":
        price = 9.60 * night * people
    elif group == "mixed":
        price = 10 * night * people
elif season == "Spring":
    if group == "boys" or group == "girls":
        price = 7.20 * night * people
    elif group == "mixed":
        price = 9.50 * night * people
elif season == "Summer":
    if group == "boys" or group == "girls":
        price = 15 * night * people
    elif group == "mixed":
        price = 20 * night * people
if 10 <= people < 20:
    price *= 0.95
elif 20 <= people < 50:
    price *= 0.85
elif people >= 50:
    price *= 0.5
if season == "Winter":
    if group == "girls":
        sport = "Gymnastics"
    elif group == "boys":
        sport = "Judo"
    elif group == "mixed":
        sport = "Ski"
elif season == "Spring":
    if group == "girls":
        sport = "Athletics"
    elif group == "boys":
        sport = "Tennis"
    elif group == "mixed":
        sport = "Cycling"
elif season == "Summer":
    if group == "girls":
        sport = "Volleyball"
    elif group == "boys":
        sport = "Football"
    elif group == "mixed":
        sport = "Swimming"
print(f'{sport} {price:.2f} lv.')



