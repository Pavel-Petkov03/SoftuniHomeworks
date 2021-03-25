# Това е четвърта задача от урок 1-Упражнения
# Трябва да се пресметне печалбата на  един магазин от лева в евро като знаем , цената и количеството на плодове и
# зеленчуци ,които той продава
price_vegetables = float(input())
price_fruits = float(input())
kg_fruits = float(input())
kg_vegetables = float(input())
bg_all = price_vegetables * kg_vegetables + price_fruits * kg_fruits
eu_all = bg_all / 1.94
print(f'{eu_all:.2f}')
