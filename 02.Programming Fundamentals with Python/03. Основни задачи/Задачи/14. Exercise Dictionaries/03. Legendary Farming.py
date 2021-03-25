# You've done all the work and the last thing left to accomplish is to own a legendary item. However, it's a
# tedious process and it requires quite a bit of farming. Anyway, you are not too pretentious – any legendary
# item will do. The possible items are:
# •	Shadowmourne – requires 250 Shards;
# •	Valanyr – requires 250 Fragments;
# •	Dragonwrath – requires 250 Motes;
# Shards, Fragments and Motes are the key materials and everything else is junk. You will be given lines of input,
# in the format:
# 2 motes 3 ores 15 stones
# Keep track of the key materials - the first one that reaches the 250 mark, wins the race. At that point you have
# to print that the corresponding legendary item is obtained. Then, print the remaining shards, fragments, motes, ordered
# by quantity in descending order, then by name in ascending order, each on a new line. Finally, print the collected junk
# items in alphabetical order.
# Input
# •	Each line comes in the following format: {quantity} {material} {quantity} {material} … {quantity} {material}
# Output
# •	On the first line, print the obtained item in the format: {Legendary item} obtained!
# •	On the next three lines, print the remaining key materials in descending order by quantity
# o	If two key materials have the same quantity, print them in alphabetical order
# •	On the final several lines, print the junk items in alphabetical order
# o	All materials are printed in format {material}: {quantity}
# o	The output should be lowercase, except for the first letter of the legendary
match = {'shards': "Shadowmourne", 'fragments': 'Valanyr', 'motes': "Dragonwrath"}
key_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
junk = {}
is_break = False
while True:
	if is_break:
		break
	line = input().split()
	for index in range(0, len(line), 2):
		quantity = int(line[index])
		key = line[index + 1].lower()
		if key in key_materials:
			key_materials[key] += quantity
		else:
			if key in junk:
				junk[key] += quantity
			else:
				junk[key] = quantity
		for key, value in key_materials.items():
			if value >= 250:
				print(f'{match[key]} obtained!')
				key_materials[key] -= 250
				is_break = True
				break
		if is_break:
			break

for material, quantity in sorted(key_materials.items(), key=lambda x: (-x[1], x[0])):
	print(f'{material}: {quantity}')
for material, quantity in sorted(junk.items(), key=lambda x: x[0]):
	print(f'{material}: {quantity}')







