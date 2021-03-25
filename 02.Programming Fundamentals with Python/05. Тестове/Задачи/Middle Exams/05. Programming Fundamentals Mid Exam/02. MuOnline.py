# You have initial health 100 and initial bitcoins 0. You will be given a string,
# representing the dungeons rooms. Each room is separated with '|' (vertical bar): "room1|room2|room3…"
# Each room contains a command and a number, separated by space. The command can be:
# •	"potion"
# o	You are healed with the number in the second part. But your health cannot exceed your initial health (100).
# o	First print: "You healed for {amount} hp.".
# o	After that, print your current health: "Current health: {health} hp.".
# •	"chest"
# o	You've found some bitcoins, the number in the second part.
# o	Print: "You found {amount} bitcoins."
# •	In any other case you are facing a monster, you are going to fight.
# The second part of the room, contains the attack of the monster.
# You should remove the monster's attack from your health.
# o	If you are not dead (health <= 0) you've slain the monster, and you should print ("You slayed {monster}.")
# o	If you've died, print "You died! Killed by {monster}." and your
# quest is over. Print the best room you`ve manage to reach: "Best room: {room}".
# If you managed to go through all the rooms in the dungeon, print on the next three lines:
# "You've made it!", "Bitcoins: {bitcoins}", "Health: {health}".
# Input / Constraints
# You receive a string, representing the dungeons rooms, separated with '|' (vertical bar): "room1|room2|room3…".

health = 100
bitcoins = 0
i_survived = True
array = input().split('|')
for room in range(len(array)):
	command, amount = array[room].split()
	amount = int(amount)
	if command == 'potion':
		if health + amount >= 100:
			gain = 100 - health
		else:
			gain = amount
		print(f'You healed for {gain} hp.')
		health += gain
		print(f'Current health: {health} hp.')

	elif command == 'chest':
		bitcoins += amount
		print(f"You found {amount} bitcoins.")
	else:
		health -= amount
		if health > 0:
			print(f"You slayed {command}.")
		else:
			print(f'You died! Killed by {command}.')
			print(f'Best room: {room + 1}')
			i_survived = False
			break

if i_survived:
	print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")
