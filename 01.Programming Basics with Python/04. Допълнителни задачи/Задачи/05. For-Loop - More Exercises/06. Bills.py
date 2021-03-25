# Напишете програма която да пресмята средният разход за месец на семейство за даден период време.
# За всеки месец разходите са следните:
# •	За ток – всеки месец е различен, ще се чете от конзолата
# •	за вода – 20 лв.
# •	за интернет – 15 лв.
# •	за други – събират се тока, водата и интернета за месеца и към сумата се прибавят 20%.
# За всеки разход трябва да се пресметне колко общо е платено за всички месеци.
# Вход
# Входът се чете от конзолата:
# •	Първи ред – месеците за които се търси средният разход – цяло число в интервала [1...100]
# •	За всеки месец – сметката за ток – реално число в интервала [1.00...1000.00]
# Да се отпечата на конзолата 5 реда:
# 1ви ред: "Electricity: {ток за всички месеци} lv"
# •	2ри ред: "Water: {вода за всички месеци} lv"
# •	3ти ред: "Internet: {интернет за всички месеци} lv"
# • 	4ти ред: "Other: {други за всички месеци} lv"
# •	5ти ред: "Average: {средно всички разходи за месец} lv"
# Всички числа трябва да са форматирана до вторият знак след запетаята.
months = int(input())
water_all = months * 20
internet_all = months * 15
water = 20
internet = 15
other = 0
electricity_all = 0
other_all = 0
for d in range(1, months + 1):
    electricity = float(input())
    other += internet + water + electricity + (internet + water + electricity) * 0.2
    electricity_all += electricity
average = (electricity_all + water_all + internet_all + other) / months

print(f'Electricity: {electricity_all:.2f} lv')
print(f'Water: {water_all:.2f} lv')
print(f'Internet: {internet_all:.2f} lv')
print(f'Other: {other:.2f} lv')
print(f'Average: {average:.2f} lv')




