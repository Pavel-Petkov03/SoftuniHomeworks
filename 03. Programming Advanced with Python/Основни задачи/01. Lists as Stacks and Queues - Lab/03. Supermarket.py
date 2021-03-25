# Write a program that reads an input consisting of a name and adds it to a queue until "End" is received. If you receive
# "Paid", print every customer name and empty the queue, otherwise we receive a client and we must add him to the
# queue. When we receive "End", we must print the count of the remaining people in the queue in the format:\
# 	"{count} people remaining."
from collections import deque
my_deque = deque()
command = input()
while command != 'End':
	if command == 'Paid':
		for c in range(len(my_deque)):
			print(my_deque.popleft())
	else:
		my_deque.append(command)
	command = input()
print(f'{len(my_deque)} people remaining.')