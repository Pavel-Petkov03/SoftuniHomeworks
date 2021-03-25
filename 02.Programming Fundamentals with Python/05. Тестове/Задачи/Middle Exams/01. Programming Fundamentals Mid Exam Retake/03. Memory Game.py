# Write a program, which receives a sequence of elements. Each element in the sequence will have a twin.
# Until the player receives "end" from the console, he will receive strings with two integers separated
# by space, which represent the indexes of elements in the sequence.
# If the player tries to cheat and enters two equal indexes or indexes which are out of bounds of the
# sequence you should add two matching elements in the following format "-{number of moves until now}a"
# at the middle of the sequence and print this message on the console:
# "Invalid input! Adding additional elements to the board"
# Input
# •	On the first line you will receive sequence of elements.
# Output
# •	Every time the player hit two matching elements you should remove them from the sequence
# and print on the console the following message:
# "Congrats! You have found matching elements - ${element}!"
# •	If the player hit two different elements, you should print on the console the following message:
# "Try again!"
# •	If the player hit all matching elements before he receives "end" from the console,
# you should print on the console the following message:
# "You have won in {number of moves until now} turns!"
# •	If the player receives "end" before he hits all matching elements, you should print on
# the console the following message:
# "Sorry you lose :(
#               {the current sequence's state}"
# Constraints
# •	All elements in the sequence will always have a matching element.
array = input().split()
command = input()
turns = 0
is_won = False
while command != "end":
	first, second = command.split()
	first = int(first)
	second = int(second)
	turns += 1
	if first < 0 or first >= len(array) or second < 0 or second >= len(array) or first == second:
		print("Invalid input! Adding additional elements to the board")
		array.insert(len(array) // 2, f"-{turns}a")
		array.insert(len(array) // 2, f"-{turns}a")
	elif array[first] == array[second]:
		print(f"Congrats! You have found matching elements - {array[first]}!")
		if second > first:
			array.pop(second)
			array.pop(first)
		else:
			array.pop(first)
			array.pop(second)
	else:
		print("Try again!")
	if len(array) == 0:
		print(f"You have won in {turns} turns!")
		is_won = True
		break
	command = input()

if not is_won:
	print("Sorry you lose :(")
	print(" ".join(array))




