# You are given an array with integers. Write a program to modify the elements after receive the commands “swap”,
# “multiply” or “decrease”.
# •	“swap {index1} {index2}” take two elements and swap their places.
# •	“multiply {index1} {index2}” take element at the 1st index and multiply it with element at 2nd index.
# Save the product at the 1st index.
# •	“decrease” decreases all elements in the array with 1.
# Input
# On the first input line you will be given the initial array values separated by a single space.
# On the next lines you will receive commands until you receive the command “end”. The commands are as follow:
# •	“swap {index1} {index2}”
# •	“multiply {index1} {index2}”
# •	“decrease”
# Output
# The output should be printed on the console and consist element of the modified array –
# separated by “, “(comma and single space).
# Constraints
# •	Commands will be: “swap”, “multiply”, “decrease” and “end”
# •	Elements of the array will be integer numbers in the range [-231...231]
# •	Count of the array elements will be in the range [2...100]
# •	Indexes will be always in the range of the array

all_ = [int(c) for c in input().split()]
def f(array):
	command = input()
	while command != 'end':
		command = command.split()
		if command[0] == 'swap':
			index1 = int(command[1])
			index2 = int(command[2])
			array[index1], array[index2] = array[index2], array[index1]
		elif command[0] == 'multiply':
			index1 = int(command[1])
			index2 = int(command[2])
			array[index1] *= array[index2]
		elif command[0] == 'decrease':
			array = [int(str(c - 1)) for c in array]

		command = input()

	return ', '.join([str(c) for c in array])

print(f(all_))
