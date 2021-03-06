# Студент трябва да пропътува n километра. Той има избор измежду три вида транспорт:
# Такси. Начална такса: 0.70 лв. Дневна тарифа: 0.79 лв. / км. Нощна тарифа: 0.90 лв. / км.
# Автобус. Дневна / нощна тарифа: 0.09 лв. / км. Може да се използва за разстояния минимум 20 км.
# Влак. Дневна / нощна тарифа: 0.06 лв. / км. Може да се използва за разстояния минимум 100 км.
# Напишете програма, която въвежда броя километри n и период от деня (ден или нощ)
# и изчислява цената на най-евтиния транспорт.
km = int(input())
time = input()
if km < 20:
    if time == 'day':
        print(f'{0.70 + 0.79 * km:.2f}')
    elif time == 'night':
        print(f'{0.70 + 0.90 * km:.2f}')
elif 20 <= km < 100:
    if time == 'day':
        print(f'{0.09 * km:.2f}')
    elif time == 'night':
        print(f'{0.09 * km:.2f}')
else:
    if time == 'day':
        print(f'{0.06 * km:.2f}')
    elif time == 'night':
        print(f'{0.06 * km:.2f}')


