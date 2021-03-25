# Write a program to calculate the winner of a car race. You will receive a list of numbers.
# Each element of the list represents the time needed to pass through that step (the index).
# There are going to be two cars. One of them starts from the left side and the other one starts
# from the right side. The middle index of the list is the finish line. The number of elements in the
# list will always be odd. Calculate the total time for each racer to reach the finish, which is the middle
# of the list, and print the winner with his total time (the racer with less time). If you have a zero in the
# list, you have to reduce the time of the racer that reached it by 20% (from his current time).
# Print the result in the following format "The winner is {left/right} with total time: {total time}".


def race(array):
	array = list(map(lambda x: int(x), array.split()))
	middle = len(array) // 2
	left = array[:middle]
	right = array[-1:middle:-1]
	first_sum = 0
	second_sum = 0
	for index in left:
		first_sum += index
		if index == 0:
			first_sum *= 0.8
	for index in right:
		second_sum += index
		if index == 0:
			second_sum *= 0.8
	if first_sum < second_sum:
		return f"The winner is left with total time: {first_sum:.1f}"
	elif second_sum < first_sum:
		return f"The winner is right with total time: {second_sum:.1f}"


our_array = input()
print(race(our_array))
