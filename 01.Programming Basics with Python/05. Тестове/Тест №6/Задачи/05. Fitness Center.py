# Задача 5. Фитнес център
# Напишете програма, която да изчислява броя на посетителите в един фитнес център. В началото програмата получава броя
# на посетителите на фитнеса и за всеки човек - дейността, която извършва във фитнеса. На края програмата трябва
# да отпечата броят трениращи за всяка една дейност ("Back", "Chest", 'Legs", "Abs") и броят клиенти, закупили продукт
# ("Protein shake", "Protein bar"). Също така - процентът трениращи (спрямо общия брой посетители) и процентът
# на клиентите, закупили продукт от фитнеса.
# Вход
# От конзолата се чете число, след това поредица от низове, всяко на отделен ред:
# •	На първия ред – броят на посетителите във фитнеса – цяло число в интервала [1...1000]
# •	За всеки един посетител на отделен ред – дейността във фитнеса – текст
# ("Back", "Chest", "Legs", "Abs", "Protein shake" или "Protein bar")
# Изход
# Да се отпечатат на конзолата 8 реда, които съдържат следната информация:
# Ред 1 -	"{брой хора трениращи гръб} - back"
# Ред 2 -	"{брой хора трениращи гърди} - chest"
# Ред 3 -	"{брой хора трениращи крака} - legs"
# Ред 4 -	"{брой хора трениращи коремни мускули} - abs"
# Ред 5 -	"{брой хора закупили протеинов шейк} - protein shake"
# Ред 6 -	"{брой хора закупили протеинов блок} - protein bar"
# Ред 7 -	"{процент на хората дошли да тренират}% - work out"
# Ред 8 -	"{процент на хората дошли да купят протеин}% - protein"
# Всички проценти трябва да са форматирани до втората цифра след десетичния знак.
members = int(input())
back = 0
chest = 0
Abs = 0
legs = 0
protein_shake = 0
protein_bar = 0
for c in range(1 , members + 1):
    activity = input()
    if activity == "Back":
        back += 1
    elif activity == "Chest":
        chest += 1
    elif activity == "Legs":
        legs += 1
    elif activity == "Abs":
        Abs += 1
    elif activity == "Protein shake":
        protein_shake += 1
    elif activity == "Protein bar":
        protein_bar += 1
workout = back + chest + legs + Abs
protein = protein_bar + protein_shake
print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{Abs} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{((workout / members) * 100):.2f}% - work out")
print(f"{((protein / members) * 100):.2f}% - protein")




