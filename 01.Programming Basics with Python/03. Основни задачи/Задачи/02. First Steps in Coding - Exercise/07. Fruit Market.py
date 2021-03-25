# Мария иска да пресметне колко пари ще и потрябват за да си купи малини ,портокали,ягоди,малини:
# Тя знае ,че малините струват два пъти по малко от ягодите, че цената на портукалите е 40% по малка от цената на
# малините , Цената на бананите е с 80 процента по ниска от цената на малините
# Тя трябва да вкара количеството на всички тези плодове в конзолата за да може да пресметне общата сума , която тя
# трябва да заплати
berries_cost = float(input())
quantity_of_bananas = float(input()) * (berries_cost / 2 - (berries_cost / 2 * 8/10))
quantity_of_oranges = float(input()) * (berries_cost / 2 - (berries_cost / 2 * 4/10))
quantity_of_raspberries = float(input()) * (berries_cost / 2)
quantity_of_berries = float(input()) * berries_cost
all_cost = quantity_of_bananas + quantity_of_oranges + quantity_of_raspberries + quantity_of_berries
print(all_cost)
