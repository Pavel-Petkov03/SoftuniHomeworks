# Това е 6 задача от урок 1-Упражнения
# Георги ще има гости вечерта и решава да ги нагости
# с паламуд, сафрид и миди. Затова отива на рибната борса, за да си купи по няколко килограма
# Oт конзолата се въвеждат цените в лева на скумрията и цацата. Също количеството на паламуд, сафрид и миди в килограми
# Колко пари ще са му необходими, за да плати сметката си, ако цените на борсата са:
# Паламуд – 60% по-скъп от скумрията
# Сафрид – 80% по-скъп от цацата
# Миди – 7.50 лв. за килограм
mackerel = float(input())  # Това е цената на скумрията за кг
sprat = float(input())  # Това е цената на цацата за килограм
bonito_kg = float(input())   # Това е количеството на паламута за кг
scad_kg = float(input())   # Това е количеството на сафрида в кг
mussels_price_all = float(input()) * 7.50  # Това е количеството на мидите
bonito_price_per_kg = mackerel + 0.6 * mackerel
scad_price_per_kg = sprat + 0.8 * sprat
scad_price_all = scad_kg * scad_price_per_kg
bonito_price_all = bonito_kg * bonito_price_per_kg
all = bonito_price_all + scad_price_all + mussels_price_all
print(f'{all:.2f}')