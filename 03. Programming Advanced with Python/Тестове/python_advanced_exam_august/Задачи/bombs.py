# You will be given two sequences of integers, representing bomb effects and bomb casings.
# You need to start from the first bomb effect and try to mix it with the last bomb casing.
# If the sum of their values is equal to any of the materials in the table below – create the
# bomb corresponding to the value and remove both bomb materials. Otherwise, just decrease the
# value of the bomb casing by 5. You need to stop combining when you have no more bomb effects or
# bomb casings, or you successfully filled the bombs pouch.
# Bombs:
# •	Datura Bombs: 40
# •	Cherry Bombs: 60
# •	Smoke Decoy Bombs: 120
# To fill the bomb pouch, Ezio needs three of each of the bomb types.
# Input
# •	On the first line, you will receive the integers representing the bomb effects, separated by ", ".
# •	On the second line, you will receive the integers representing the bomb casings, separated by ", ".
# Output
# •	On the first line, print:
# o	if Ezio succeeded to fulfill the bomb pouch: "Bene! You have successfully filled the bomb pouch!"
# o	if Ezio didn't succeed to fulfill the bomb pouch: "You don't have enough materials to fill the bomb pouch."
# •	On the second line, print all bomb effects left:
# o	If there are no bomb effects: "Bomb Effects: empty"
# o	If there are effects: "Bomb Effects: {bombEffect1}, {bombEffect2}, (…)"
# •	On the third line, print all bomb casings left:
# o	If there are no bomb casings: "Bomb Casings: empty"
# o	If there are casings: "Bomb Casings: {bombCasing1}, {bombCasing2}, (…)"
# •	Then, you need to print all bombs and the count you have of them, ordered alphabetically:
# o	"Cherry Bombs: {count}"
# o	"Datura Bombs: {count}"
# o	"Smoke Decoy Bombs: {count}"
# Constraints
# •	All of the given numbers will be valid integers in the range [0, 120].
# •	There will be no cases with negative material.


from collections import deque

template_dict = {'Datura Bombs': 0, 'Cherry Bombs': 0, 'Smoke Decoy Bombs': 0}
bomb_effect = deque(list(map(int, input().split(', '))))
bomb_casing = list(map(int, input().split(', ')))


def adding(n):
    global template_dict
    if n == 40:
        template_dict['Datura Bombs'] += 1
        return True
    elif n == 60:
        template_dict['Cherry Bombs'] += 1
        return True
    elif n == 120:
        template_dict['Smoke Decoy Bombs'] += 1
        return True
    return False


is_done = False
while bomb_casing and bomb_effect:
    sum_value = bomb_effect[0] + bomb_casing[-1]
    if adding(sum_value):
        bomb_effect.popleft()
        bomb_casing.pop()
    else:
        bomb_casing[-1] -= 5
    if len([True for key, value in template_dict.items() if value >= 3]) == 3:
        is_done = True
        break

if is_done:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if bomb_effect:
    bomb_effect_result = f"Bomb Effects: {', '.join(list(map(str, bomb_effect)))}"
else:
    bomb_effect_result = f"Bomb Effects: empty"
if bomb_casing:
    bomb_casing_result = f"Bomb Casings: {', '.join(list(map(str, bomb_casing)))}"
else:
    bomb_casing_result = "Bomb Casings: empty"

print(bomb_effect_result)
print(bomb_casing_result)
for key, value in sorted(template_dict.items(), key=lambda x: x[0]):
    print(f"{key}: {value}")
