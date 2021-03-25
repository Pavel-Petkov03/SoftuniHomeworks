# Деси трябва да заведе котката си на ветеринар в клиниката "Happy Cat", но паркингът се заплаща. Напишете програма, която пресмята колко общо трябва да се плати за престоя на колата на Деси на паркинга, за да заведе котката си на ветеринар. Паркингът е различен от останалите и има разнообразен ценоразпис. За всеки четен ден и нечетен час, паркингът таксува 2.50 лева. Във всеки нечетен ден и четен час таксата е 1.25 лева, във всички останали случаи се заплаща 1 лев. Таксуването става на всеки изминал час от деня. Всеки един от изходите трябва да бъде закръглен до втория знак след десетичната запетая.
# Вход
# От конзолата се четат два реда:
# •	Брой дни – цяло число в интервала [1 … 5]
# •	Брой часове за всеки един от дните - цяло число в интервала [1 … 24]
# Изход:
# Да се отпечата на конзолата:
# •	За всеки изминал ден, общата сума, която трябва да се плати – "Day: {индексът на деня} – {общата сума за деня} leva"
# •	Когато програмата приключи - "Total: {общата сума за всички дни} leva"
days = int(input())
hours = int(input())
charge = 0
final_charge = 0
for day in range(1 , days + 1):
    charge = 0
    for hour in range(1 , hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            charge += 2.5
        elif day % 2 != 0 and hour % 2 == 0:
            charge += 1.25
        else:
            charge += 1
    final_charge += charge
    print(f"Day: {day} - {charge:.2f} leva")
print(f"Total: {final_charge:.2f} leva")