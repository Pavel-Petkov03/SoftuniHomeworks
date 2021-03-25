# As a gladiator, Peter has to repair his broken equipment when he loses a fight.
# His equipment consists of helmet, sword, shield and armor. You will receive the Peter`s lost fights count.
# Every second lost game, his helmet is broken.
# Every third lost game, his sword is broken.
# When both his sword and helmet are broken in the same lost fight, his shield also brakes.
# Every second time, when his shield brakes, his armor also needs to be repaired.
# You will receive the price of each item in his equipment.
# Calculate his expenses for the year for renewing his equipment.
# Input / Constraints
# The input will consist of 5 lines:
# •	On the first line you will receive the lost fights count – integer in the range [0, 1000].
# •	On the second line you will receive the helmet price - floating point number in range [0, 1000].
# •	On the third line you will receive the sword price - floating point number in range [0, 1000].
# •	On the fourth line you will receive the shield price - floating point number in range [0, 1000].
# •	On the fifth line you will receive the armor price - floating point number in range [0, 1000].
# Output
# •	As output you must print Peter`s total expenses for new equipment: "Gladiator expenses: {expenses} aureus"
looses = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price= float(input())
armor_price = float(input())
helmet = 0
sword = 0
shield = 0
armor = 0
is_broken_helmet = False
is_broken_sword = False
is_broken_shield = False
times = 0
for lose in range(1, looses + 1):
    if lose % 2 == 0:
        helmet += 1
        is_broken_helmet = True
    else:
        is_broken_helmet = False
    if lose % 3 == 0:
        sword += 1
        is_broken_sword = True
    else:
        is_broken_sword = False
    if is_broken_helmet and is_broken_sword:
        shield += 1
        times += 1
        is_broken_shield = True
    else:
        is_broken_shield = False
    if lose % 2 == 0 and times == 2:
        armor += 1
        times = 0
price = armor * armor_price + shield * shield_price + sword * sword_price + helmet * helmet_price
print(f'Gladiator expenses: {price:.2f} aureus')


