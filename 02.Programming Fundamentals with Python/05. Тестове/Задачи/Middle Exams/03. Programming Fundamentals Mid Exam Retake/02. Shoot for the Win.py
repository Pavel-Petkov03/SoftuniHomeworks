# Write a program to read a sequence of integers and find and print the top 5 numbers that are greater
# than the average value in the sequence, sorted in descending order.
# Input
# Read from the console a single line holding space separated number.
# Output
# Print the above described numbers on a single line, space separated. If less than 5 numbers hold the
# above mentioned property, print less than 5 numbers. Print “No” if no numbers hold the above property.
# Constraints
# All input numbers are integers in range [-1 000 000 … 1 000 000]. The count of numbers is in range [1…10 000].

array = [int(c) for c in input().split()]
command = input()
while command != 'End':
	index = int(command)
	if 0 <= index <= len(array) - 1:
		wanted_value = array[index]
		array[index] = -1
		for i, c in enumerate(array):
			if c != -1:
				if c > wanted_value:
					array[i] -= wanted_value
				else:
					array[i] += wanted_value

	command = input()

shot = [c for c in array if c == -1]
print(f'Shot targets: {len(shot)} -> {" ".join([str(c) for c in array])}')

