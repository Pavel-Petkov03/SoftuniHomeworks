# Магазин за компютърни игри ви наема за да направите статистика на процента продажби на игрите от последния месец, като изчислите по колко процента от общите продажби са за някоя от игрите.
# Процентите трябва да бъдат разделени на четири части, три заглавия на игри и всички останали :
# •	Hearthstone
# •	Fornite
# •	Overwatch
# •	Others
# Вход
# От конзолата се четат:
# •	Брой продадени игри- n - цяло положително число в интервала [1… 100]
# За следващите n реда се чете по един ред:
# o	Име на игра - текст
# Изход
# На конзолата да се изпишат четири реда:
# 	"Hearthstone - {процент продажби на Hearthstone}%"
# 	"Fornite - {процент продажби на Fornite}%"
# 	"Overwatch - {процент продажби на Overwatch}%"
# 	"Others - {процент продажби на всички останали игри}%"
# Резултатът да бъде закръглен до втората цифра след десетичния знак.
times = int(input())
total = 0
fortnite = 0
over = 0
hearth = 0
other = 0
for c in range(1 , times + 1):
    name = input()
    total += 1
    if name == "Hearthstone":
        hearth += 1
    elif name == "Fornite":
        fortnite += 1
    elif name == "Overwatch":
        over += 1
    else:
        other += 1
print(f'Hearthstone - {(hearth / total * 100):.2f}%')
print(f"Fornite - {(fortnite / total  *100):.2f}%")
print(f"Overwatch - {(over / total * 100):.2f}%")
print(f"Others - {(other / total * 100):.2f}%")