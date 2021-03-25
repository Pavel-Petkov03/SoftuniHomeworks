# Петър иска да купи N видеокарти, M процесора и P на брой рам памет. Ако броя на видеокартите е по-голям от този на процесорите получава 15% отстъпка от крайната сметка. Важат следните цени:
# •	Видеокарта – 250 лв./бр.
# •	Процесор – 35% от цената на закупените видеокарти/бр.
# •	Рам памет – 10% от цената на закупените видеокарти/бр.
# Да се изчисли нужната сума за закупуване на материалите и да се пресметне дали бюджета ще му стигне.
# Вход
# Входът се състои от четири реда:
# 1.	Бюджетът на Петър - реално число в интервала [0.0…100000.0]
# 2.	Броят видеокарти - цяло число в интервала [0…100]
# 3.	Броят процесори - цяло число в интервала [0…100]
# 4.	Броят рам памет - цяло число в интервала [0…100]
# Изход
# На конзолата се отпечатва 1 ред, който трябва да изглежда по следния начин:
# •	Ако бюджета е достатъчен:
# "You have {остатъчен бюджет} leva left!"
# •	Ако сумата надхвърля бюджета:
# "Not enough money! You need {нужна сума} leva more!"
# Резултатът да се форматира до втория знак след десетичната запетая.
budget = float(input())
video_cards = int(input())
processors = int(input())
ram_memory = int(input())
all_video_cards = 250 * video_cards
processors_price = processors * (0.35 * all_video_cards)
ram_memory_price = ram_memory * (0.1 * all_video_cards)
all_price = all_video_cards + processors_price + ram_memory_price
if video_cards > processors:
    all_price *= 0.85
if budget >= all_price:
    print(f"You have {abs(budget - all_price):.2f} leva left!")
else:
    print(f"Not enough money! You need {abs(budget - all_price):.2f} leva more!")

