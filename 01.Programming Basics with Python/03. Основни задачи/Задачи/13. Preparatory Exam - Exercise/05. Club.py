# Линк към Judge: https://judge.softuni.bg/Contests/Practice/Index/1745#6
# Времето се затопля и клубовете пускат обещаващи промоции. Напише програма, която да изчислява приходите на един клуб за вечерта и дали е достигната желаната печалба, като знаете следните условия: цената на един коктейл е дължината неговото име. Ако цената на една поръчка е нечетно число, има 25% отстъпка от цената на поръчката.
# Вход
# От конзолата се четат:
# •	На първия ред – желаната печалба на клуба - реално число в интервала [1.00... 15000.00]
# Поредица от два реда до получаване на командата "Party!" или до достигане на желаната печалба:
# o	Име на коктейла – текст
# o	Брой на коктейлите за поръчката – цяло число в интервала [1… 50]
# Изход
# На конзолата първо да се отпечата един ред:
# •	При получена команда "Party!":
#  "We need {недостигаща сума} leva more."
# •	При достигане на желаната печалба:
# 	"Target acquired."
# След това да се отпечата:
# 	"Club income - {приходи от клуба} leva."
# Парите да бъдат форматирани до втората цифра след десетичния знак.
members = int(input())
back = 0
chest = 0
Abs = 0
legs = 0
protein_shake = 0
protein_bar = 0
for c in range(1 , members + 1):
    activity = input()
    if activity == "Back":
        back += 1
    elif activity == "Chest":
        chest += 1
    elif activity == "Legs":
        legs += 1
    elif activity == "Abs":
        Abs += 1
    elif activity == "Protein shake":
        protein_shake += 1
    elif activity == "Protein bar":
        protein_bar += 1
workout = back + chest + legs + Abs
protein = protein_bar + protein_shake
print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{Abs} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{((workout / members) * 100):.2f}% - work out")
print(f"{((protein / members) * 100):.2f}% - protein")