# You own a fashion boutique and you receive a delivery once a month in a huge box,
# which is full of clothes. You must arrange them in your store, so you take the box and start
# from the last piece of clothing on the top of the pile to the first one at the bottom.
# Use a stack for the purpose. Each piece of clothing has its value (an integer). You must
# sum their values, while you take them out of the box. You will be given an integer representing
# the capacity of a rack. While the sum of the clothes is less than the capacity, keep summing them.
# If the sum becomes equal to the capacity you must take a new rack for the next clothes, if there are
# any left in the box. If it becomes greater than the capacity, don't add the piece of clothing to the
# current rack and take a new one. In the end, print how many racks you have used to hang must the clothes.
# Input
# •	On the first line you will be given a sequence of integers, representing the clothes in the
# box, separated by a single space.
# •	On the second line, you will be given an integer, representing the capacity of a rack.
# Output
# •	Print the number of racks, needed to hang must the clothes from the box.
# Constraints
# •	The values of the clothes will be integers in the range [0,20]
# •	There will never be more than 50 clothes in a box
# •	The capacity will be an integer in the range [0,20]
# •	None of the integers from the box will be greater than then the value of the capacity


stack = [int(c) for c in input().split()]
rack_quantity = int(input())
initial_rack = rack_quantity
counter = 0
while stack:
	taken = stack[-1]
	if taken > rack_quantity:
		counter += 1
		rack_quantity = initial_rack
	else:
		rack_quantity -= taken
		stack.pop()
		if len(stack) == 1:
			counter += 1

# 5 4 8 6 3 8 7 7 9
print(counter)
