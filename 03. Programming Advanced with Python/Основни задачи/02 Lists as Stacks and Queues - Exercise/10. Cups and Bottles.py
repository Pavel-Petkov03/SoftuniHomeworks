# You will be given a sequence of integers – each indicating a cup's capacity. After that you will be given another
# sequence of integers – a bottle with water in it. Your job is to try to fill up all the cups.
# Filling is done by picking exactly one bottle at a time. You must start picking from the last received bottle and
# start filling from the first entered cup. If the current bottle has N water, you give the first entered cup N water
# and reduce its integer value by N.
# When a cup's integer value reaches 0 or less, it gets removed. It is possible that the current cup's value is greater
# than the current bottle's value. In that case you pick bottles until you reduce the cup's integer value to 0 or less.
# If a bottle's value is greater or equal to the cup's current value, you fill up the cup and the remaining water
# becomes wasted. You should keep track of the wasted litters of water and print it at the end of the program.
# If you have managed to fill up all the cups, print the remaining water bottles, from the last entered – to the first,
# otherwise you must print the remaining cups, by order of entrance – from the first entered – to the last.
# Input
# •	On the first line of input you will receive the integers,
# representing the cups' capacity, separated by a single space.
# •	On the second line of input you will receive the integers,
# representing the filled bottles, separated by a single space.
# Output
# •	On the first line of output you must print the remaining bottles, or the remaining cups, depending on the case
# you are in. Just keep the orders of printing exactly as specified.
# o	"Bottles: {remaining_bottles}" or "Cups: {remaining_cups}"
# •	On the second line print the wasted litters of water in the following format: "Wasted litters of water:
# {wastedLitters_of_water}."
# Constraints
# •	All the given numbers will be valid integers in the range [1, 500].
# •	It is safe to assume that there will be NO case in which the water is exactly as much as the cups' values,
# so that at the end there are no cups and no water in the bottles.


from collections import deque
cups_capacity = deque([int(c) for c in input().split()])
bottles_fill = [int(c) for c in input().split()]
lost = 0
while len(cups_capacity) > 0 and len(bottles_fill) > 0:
	current_bottle = bottles_fill.pop()
	if current_bottle >= cups_capacity[0]:
		lost += current_bottle - cups_capacity.popleft()
	else:
		cups_capacity[0] -= current_bottle

if bottles_fill:
	print(f"Bottles: {' '.join([str(c) for c in reversed(bottles_fill)])}")
	print( f'Wasted litters of water: {lost}')
elif cups_capacity:
	print(f'Cups: {" ".join([str(c) for c in cups_capacity])}')
	print(f'Wasted litters of water: {lost}')
