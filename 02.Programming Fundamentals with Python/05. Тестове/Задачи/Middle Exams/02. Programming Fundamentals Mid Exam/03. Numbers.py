# Write a program to read a sequence of integers and find and print the top 5 numbers that are greater
# than the average value in the sequence, sorted in descending order.
# Input
# Read from the console a single line holding space separated number.
# Output
# Print the above described numbers on a single line, space separated. If less than 5 numbers
# hold the above mentioned property, print less than 5 numbers. Print “No” if no numbers hold the above property.
# Constraints
# All input numbers are integers in range [-1 000 000 … 1 000 000]. The count of numbers is in range [1…10 000].

all_= [int(c) for c in input().split()]
average = sum([int(c) for c in all_]) / len(all_)
final = []
for c in sorted(all_, reverse=True):
	if len(final) < 5 and int(c) > average:
		final.append(int(c))

if len(final) == 0:
	print("No")
else:
	a = sorted([int(c) for c in final], reverse=True)
	a = [str(c) for c in a]
	print(' '.join(a))

