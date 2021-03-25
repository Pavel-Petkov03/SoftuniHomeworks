# Heroes III is the best game ever. Everyone loves it and everyone plays it all the time. Stamat is no exclusion
# to this rule. His favorite units in the game are all types of dragons – black, red, gold, azure etc…
# He likes them so much that he gives them names and keeps logs of their stats: damage, health and armor.
# The process of aggregating all the data is quite tedious, so he would like to have a program doing it.
# Since he is no programmer, it's your task to help him.
# You need to categorize dragons by their type. For each dragon, identified by name, keep information about
# his stats. Type is preserved as in the order of input, but dragons are sorted alphabetically by name.
# For each type, you should also print the average damage, health and armor of the dragons. For each dragon,
# print his own stats.
# There may be missing stats in the input, though. If a stat is missing you should assign it default values.
# Default values are as follows: health 250, damage 45, and armor 10. Missing stat will be marked by null.
# The input is in the following format {type} {name} {damage} {health} {armor}. Any of the integers may be
# assigned null value. See the examples below for better understanding of your task.
# If the same dragon is added a second time, the new stats should overwrite the previous ones. Two dragons
# are considered equal if they match by both name and type.
# Input
# •	On the first line, you are given number N -> the number of dragons to follow
# •	On the next N lines, you are given input in the above described format.
# There will be single space separating each element.
# Output
# •	Print the aggregated data on the console
# •	For each type, print average stats of its dragons in format {Type}::({damage}/{health}/{armor})
# •	Damage, health and armor should be rounded to two digits after the decimal separator
# •	For each dragon, print its stats in format -{Name} -> damage: {damage}, health: {health}, armor: {armor}
# Constraints
# •	N is in range [1…100]
# •	The dragon type and name are one word only, starting with capital letter.
# •	Damage health and armor are integers in range [0 … 100000] or null

def add_(dict_, color_, name_, dmg_, hp_, armor_):
	if dmg_ == "null" or hp_ == "null" or armor_ == "null":
		if dmg_ == "null":
			dmg_ = 45
		if hp_ == "null":
			hp_ = 250
		if armor_ == "null":
			armor_ = 10

	dmg_ = int(dmg_)
	armor_ = int(armor_)
	hp_ = int(hp_)

	if color_ in dict_:
		dict_[color_][name_] = [dmg_, hp_, armor_]
	else:
		dict_[color_] = {name_: [dmg_, hp_, armor_]}

	return dict_


our_dict = {}
average_dict = {}
n = int(input())
for time in range(n):
	command = input()
	color, name, dmg, hp, armor = command.split()
	our_dict = add_(our_dict, color, name, dmg, hp, armor)

for colors, name_and_items in our_dict.items():
	average_dict[colors] = [0, 0, 0]
	for name, items in name_and_items.items():
		for index in range(len(items)):
			average_dict[colors][index] += int(our_dict[colors][name][index])
	average_dict[colors] = [f'{(average_dict[colors][0] / len(our_dict[colors])):.2f}', f'{(average_dict[colors][1] / len(our_dict[colors])):.2f}', f'{(average_dict[colors][2] / len(our_dict[colors])):.2f}']

for color, massive in average_dict.items():
	print(f'{color}::({massive[0]}/{massive[1]}/{massive[2]})')
	for name, massive2 in sorted(our_dict[color].items(), key=lambda x: x[0]):
		print(f'-{name} -> damage: {massive2[0]}, health: {massive2[1]}, armor: {massive2[2]}')

