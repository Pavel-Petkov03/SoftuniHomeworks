# Марин и Нели си купуват къща недалеч от София.
# Нели толкова много обича цветята,
# че Ви убеждава да напишете програма, която да изчисли колко  ще им струва,
# за да засадят определен брой цветя и дали наличният бюджет ще им е достатъчен.
# Различните цветя са с различни цени:
# цвете	Роза	Далия	Лале	Нарцис	Гладиола
# Цена на брой в лева	5	3.80	2.80	3	2.50
# Съществуват следните отстъпки:
# Ако Нели купи повече от 80 Рози - 10% отстъпка от крайната цена;
# Ако Нели купи повече от 90  Далии - 15% отстъпка от крайната цена;
# Ако Нели купи повече от 80 Лалета - 15% отстъпка от крайната цена;
# Ако Нели купи по-малко от 120 Нарциса - цената се оскъпява с 15%;
# Ако Нели Купи по-малко от 80 Гладиоли - цената се оскъпява с 20%.
# От конзолата се четат 3 реда:
# Вид цветя - текст с възможности "Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus";
# Брой цветя - цяло число;
# Бюджет - цяло число.
# Да се отпечата на конзолата на един ред:
# Ако бюджетът им е достатъчен -
# "Hey, you have a great garden with {броя цвета} {вид цветя} and {останалата сума} leva left.";
# Ако бюджета им е НЕ достатъчен - "Not enough money, you need {нужната сума} leva more.".
# Сумата да бъде форматирана до втория знак след десетичната запетая.
kind = input()
count = int(input())
budget = int(input())
all_cost = float()
discount = float()
if kind == "Roses":
    all_cost = 5 * count
    if count > 80:
        discount = all_cost - 0.1 * all_cost
    else:
        discount = all_cost
elif kind == "Dahlias":
    all_cost = 3.80 * count
    if count > 90:
        discount = all_cost - 0.15 * all_cost
    else:
        discount = all_cost
elif kind == "Tulips":
    all_cost = 2.80 * count
    if count > 80:
        discount = all_cost - 0.15 * all_cost
    else:
        discount = all_cost
elif kind == "Narcissus":
    all_cost = 3 * count
    if count < 120:
        discount = all_cost + 0.15 * all_cost
    else:
        discount = all_cost
elif kind == "Gladiolus":
    all_cost = 2.50 * count
    if count < 80:
        discount = all_cost + 0.20 * all_cost
    else:
        discount = all_cost
if budget >= discount:
    print(f"Hey, you have a great garden with {count} {kind} and {(budget - discount):.2f} leva left.")
else:
    print(f"Not enough money, you need {(discount - budget):.2f} leva more.")

