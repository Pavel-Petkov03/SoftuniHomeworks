# Джеси решава, че иска да се занимава с баскетбол, но за да тренира е нужна екипировка. Напишете програма,
# която изчислява какви разходи ще има Джеси, ако започне да тренира, като знаете
# колко е таксата за тренировки по баскетбол за
# период от 1 година. Нужна екипировка:
# •	Баскетболни кецове – цената им е 40% по-малка от таксата за една година
# •	Баскетболен екип – цената му е 20% по-евтина от тази на кецовете
# •	Баскетболна топка – цената ѝ е 1 / 4 от цената на баскетболния екип
# •	Баскетболни аксесоари – цената им е 1 / 5 от цената на баскетболната топка
# Вход
# От конзолата се четe 1 ред:
# •	Годишната такса за тренировки по баскетбол – цяло число в интервала [0… 999]
# Изход
# Да се отпечата на конзолата колко ще са разходите на Джеси, ако започне да спортува баскетбол.
# Сумата да бъде форматирана до втория знак след десетичния знак.
year = int(input())
basketball_shoes = 0.6 * year
basketball_equipment = 0.8 * basketball_shoes
basketball_ball = basketball_equipment / 4
basketball_acsesuars = basketball_ball / 5
all_price = year + basketball_acsesuars + basketball_ball + basketball_equipment + basketball_shoes
print(f'{all_price:.2f}')