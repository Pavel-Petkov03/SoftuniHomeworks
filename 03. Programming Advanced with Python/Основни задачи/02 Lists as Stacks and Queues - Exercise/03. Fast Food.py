# You have a fast food restaurant and most of the food that you're offering is previously prepared.
# You need to know if you will have enough food to serve lunch to all your customers.
# Write a program that checks the orders' quantity. You also want to know the client with the biggest
# order for the day, because you want to give him a discount the next time he comes.
# First, you will be given the quantity of the food that you have for the day (an integer number). Next,
# you will be given a sequence of integers, each representing the quantity of an order. Keep the orders in a
# queue. Find the biggest order and print it. You will begin servicing your clients from the first one that came.
# Before each order, check if you have enough food left to complete it. If you have, remove the order from the queue
# and reduce the amount of food you have. If you succeeded in servicing all your clients, print:
# "Orders complete".
#  If not, print:
# "Orders left: {order1} {order2} .... {orderN}".
# Input
# •	On the first line you will be given the quantity of your food - an integer in the range [0, 1000]
# •	On the second line you will receive a sequence of integers, representing each order, separated by a single space
# Output
# •	Print the quantity of biggest order
# •	Print "Orders complete" if the orders are complete

from collections import deque
all_c = int(input())

my_deque = deque([int(c) for c in input().split()])
print(max(my_deque))
is_break = False
while len(my_deque):
	if all_c >= my_deque[0]:
		all_c -= my_deque[0]
		my_deque.popleft()
	else:
		is_break = True
		break

if is_break:
	print(f'Orders left: {" ".join([str(my_deque.popleft()) for c in range(len(my_deque))])}')
else:
	print("Orders complete")
