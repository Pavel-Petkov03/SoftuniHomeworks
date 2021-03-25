# Suppose there is a circle. There are N petrol pumps on that circle. Petrol pumps are numbered 0 to (N−1)
# (both inclusive). You have two pieces of information corresponding to each of the petrol pump: (1) the amount
# of petrol that petrol pump will give, and (2) the distance from that petrol pump to the next petrol pump
# (kilometers).
# Initially, you have a tank of infinite capacity carrying no petrol. You can start the tour at any of the petrol
# pumps. Calculate the first point from where the truck will be able to complete the circle. Consider that the
# truck will stop at each of the petrol pumps. The truck will move one kilometer for each liter of the petrol.
# Input
# •	The first line will contain the value of N
# •	The next N lines will contain a pair of integers each, i.e. the amount of petrol that petrol pump will
# give and the distance between that petrol pump and the next petrol pump

from collections import deque
n = int(input())
my_deque = deque([[int(c) for c in input().split()] for c in range(n)])
my_liters = 0
is_done = False
index = None
for c in range(n):
	for index in range(n):
		liters = my_deque[index][0]
		km = my_deque[index][1]
		my_liters += liters
		if km > my_liters:
			my_liters = 0
			my_deque.append(my_deque.popleft())
			is_done = False
			break
		else:
			my_liters -= km
			is_done = True
	if is_done:
		index = c
		break
print(index)




