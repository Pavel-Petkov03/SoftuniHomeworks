# Write a program that reads on the first line the starting quantity of water in a dispenser.
# Then on the next few lines you will be given the names of some people that want to get water
# (each on separate line) until you receive the command "Start". Add those people in a queue.
# Finally, you will receive some commands until the command "End":
# -	{liters} - Litters that the current person in the queue wants to get. Check if there is enough
# water in the dispenser for that person.
# o	If there is enough water, print "{person_name} got water" and remove him/her from the queue.
# o	Otherwise, print "{person} must wait" and remove the person from the queue without reducing the
# water in the dispenser
# -	refill {liters} - add the given litters in the dispenser.
# At the end print how many litters of water are left in the format: "{left_liters} liters left"

from collections import deque
my_deque = deque()
liters = int(input())
command = input()
while command != 'Start':
	my_deque.append(command)
	command = input()

command = input()
while command != 'End':
	if command.split()[0] == 'refill':
		liters += int(command.split()[1])
	else:
		quantity = int(command)
		if quantity > liters:
			print( f"{my_deque.popleft()} must wait" )
		else:
			print( f'{my_deque.popleft()} got water' )
			liters -= quantity

	command = input()

print(f'{liters} liters left')

