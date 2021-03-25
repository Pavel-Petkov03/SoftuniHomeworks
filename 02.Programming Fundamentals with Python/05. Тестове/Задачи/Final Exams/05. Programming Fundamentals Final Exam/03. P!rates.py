# Anno 1681. The Caribbean. The golden age of piracy. You are a well-known pirate captain by the name of Jack…
# Daniels. Together with your comrades Jim (Beam) and Johnny (Walker) you have been roaming the seas, looking
# for gold and treasure… and the occasional killing, of course. Go ahead, target some wealthy settlements and
# show them the pirate`s way!
# Description
# Until the "Sail" command is given you will be receiving:
# •	Cities that you and your crew have targeted, with their population and gold, separated by "||".
# •	If you receive a city which has been already received, you have to increase the population and gold with
# the given values.
# After the "Sail" command, you will start receiving lines of text representing events until the "End" command is given.
# Events will be in the following format:
# •	"Plunder=>{town}=>{people}=>{gold}"
# o	You have successfully attacked and plundered the town, killing the given number of people and
# stealing the respective amount of gold.
# o	For every town you attack print this message: "{town} plundered! {gold} gold stolen, {people} citizens killed."
# o	If any of those two values (population or gold) reaches zero, the town is disbanded.
# 	You need to remove it from your collection of targeted cities and print the following message:
# "{town} has been wiped off the map!"
# o	There will be no case of receiving more people or gold than there is in the city.
# •	"Prosper=>{town}=>{gold}"
# o	There has been a dramatic economic growth in the given city, increasing its treasury by the given amount of gold.
# o	The gold amount can be a negative number, so be careful. If a negative amount of gold is given
# print: "Gold added cannot be a negative number!" and ignore the command.
# o	If the given gold is a valid amount, increase the town's gold reserves by the respective amount
# and print the following message: "{gold added} gold added to the city treasury. {town} now has {total gold} gold."
# Input
# •	On the first lines, until the "Sail" command, you will be receiving strings representing the cities
# with their gold and population, separated by "||"
# •	On the next lines, until the "End" command, you will be receiving strings representing the actions
# described above, separated by "=>"
# Output
# •	After receiving the "End" command if there are any existing settlements on your list of targets, you
# need to print all of them, sorted by their gold in descending order, then by their name in ascending order,
# in the following format:
# Ahoy, Captain! There are {count} wealthy settlements to go to:
# {town1} -> Population: {people} citizens, Gold: {gold} kg
#    …
# {town…n} -> Population: {people} citizens, Gold: {gold} kg
# •	If there are no settlements left to plunder, print:
# "Ahoy, Captain! All targets have been plundered and destroyed!"
# Constraints
# •	The initial population and gold of the settlements will be valid, 32-bit integers,
# will never be negative or exceed the respective limits.
# •	The town names in the events will always be valid towns that should be on your list.
# Examples
our_dict = {}
command = input()
while command != 'Sail':
	name , p , g = command.split("||")
	if name in our_dict:
		our_dict[name][0] += int(p)
		our_dict[name][1] += int(g)
	else:
		our_dict[name] = [int(p), int(g)]
	command = input()

command = input()
while command != 'End':
	c = command.split("=>")
	if len(c) == 4:
		_ , town , people , gold = c
		if _ == 'Plunder':
			print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
			our_dict[town][0] -= int(people)
			our_dict[town][1] -= int(gold)
			if 0 in our_dict[town]:
				print(f"{town} has been wiped off the map!")
				our_dict.pop(town)
	elif len(c) == 3:
		_, town, gold = c
		if _ == 'Prosper':
			if int(gold) < 0:
				print("Gold added cannot be a negative number!" )
			else:
				our_dict[town][1] += int(gold)
				print(f"{gold} gold added to the city treasury. {town} now has {our_dict[town][1]} gold.")
	command = input()

print(f'Ahoy, Captain! There are {len(our_dict)} wealthy settlements to go to:')

if len(our_dict) == 0:
	print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
	for key , value in sorted(our_dict.items() , key = lambda z: (-z[1][1] , z[0])):
		print(f'{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg')
