# Задача 4. Кино
# От кино ви наемат да напишете програма, чрез която да разберете дали на една прожекцията ще се запълни залата и
# колко пари ще се изкарат от нея. Получавате места в залата и на всеки следващ ред до команда "Movie time!",
# колко хора влизат в залата. Цената на един билет е 5 лв. Ако текущия брой хора влезли в залата се дели на
# 3 без остатък, се прави отстъпка 5лв от общата им сметка.
# Ако в залата се опитат да влязат повече хора от колкото места са останали, то се счита че местата са изчерпани и
# програмата трябва да приключи четенето на вход.
# Вход
# От конзолата се четат:
# •	На първия ред - капацитет на залата - цяло число в интервала [50... 150]
# На всеки следващ ред до команда "Movie time!":
# o	Брой хора влизащи в киното - цяло число в интервала [1… 15]
# Изход
# На конзолата първо да се отпечата един ред:
# •	При получена команда "Movie time!":
#  "There are {останали места} seats left in the cinema."
# •	При изчерпване на местата в залата:
# 	"The cinema is full."
# След това да се отпечата:
# 	"Cinema income - {приходи от залата} lv."
capacity = int(input())
command = input()
price = 0
all_price = 0
is_full = False
while command != "Movie time!":
    people = int(command)
    capacity -= people
    if capacity < 0:
        is_full = True
        break
    if people % 3 == 0:
        price = people * 5 - 5
    else:
        price = people * 5
    all_price += price
    command = input()
if is_full:
    print("The cinema is full.")
else:
    print(f"There are {capacity} seats left in the cinema.")
print(f"Cinema income - {all_price} lv.")

