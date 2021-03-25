# Когато пуснали билетите за Евро 2016, група запалянковци решили да си закупят.
# Билетите имат две категории с различни цени:
# 3Запалянковците имат определен бюджет, а броят на хората в групата определя какъв процент
# от бюджета трябва да се задели за транспорт:
# •	От 1 до 4 – 75% от бюджета.
# •	От 5 до 9 – 60% от бюджета.
# •	От 10 до 24 – 50% от бюджета.
# •	От 25 до 49 – 40% от бюджета.
# •	50 или повече – 25% от бюджета.
# Вход
# Входът се чете от конзолата и съдържа точно 3 реда:
# •	На първия ред е бюджетът – реално число в интервала [1 000.00 ... 1 000 000.00]
# •	На втория ред е категорията – "VIP" или "Normal"
# •	На третия ред е броят на хората в групата – цяло число в интервала [1 ... 200]
# Изход
# Да се отпечата на конзолата един ред:
# •	Ако бюджетът е достатъчен:
# o	"Yes! You have {останалите пари на групата} leva left."
# •	Ако бюджетът НЕ Е достатъчен:
# o	"Not enough money! You need {сумата, която не достига} leva."
# Сумите трябва да са форматирани с точност до два знака след десетичната запетая
budget = float(input())
category = input()
count = int(input())
if 1 <= count <= 4:
    budget *= 0.25
    if category == "Normal":
        budget = budget - count * 249.99
    elif category == "VIP":
        budget = budget - count * 499.99
elif 5 <= count <= 9:
    budget *= 0.4
    if category == "Normal":
        budget = budget - count * 249.99
    elif category == "VIP":
        budget = budget - count * 499.99
elif 10 <= count <= 24:
    budget *= 0.5
    if category == "Normal":
        budget = budget - count * 249.99
    elif category == "VIP":
        budget = budget - count * 499.99
elif 25 <= count <= 49:
    budget *= 0.6
    if category == "Normal":
        budget = budget - count * 249.99
    elif category == "VIP":
        budget = budget - count * 499.99
elif count >= 50:
    budget *= 0.75
    if category == "Normal":
        budget = budget - count * 249.99
    elif category == "VIP":
        budget = budget - count * 499.99
if budget >= 0:
    print(f"Yes! You have {budget:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(budget):.2f} leva.")

