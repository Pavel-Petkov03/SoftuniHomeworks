# You will receive a number N. On the next N lines, you will be receiving names.
# You must sum the ascii values of each letter in the name and integer divide it to the value of the current line.
# Save the devised number to a set of either odd or even numbers, depending if it's an odd or even number.
# After that, sum the values of the odd and even numbers.
# •	If the summed numbers are equal, print the union values, separated by ", ".
# •	If the odd sum is bigger than the even, print the different values, separated by ", ".
# •	If the even sum is bigger than the odd, print the symmetric different values, separated by ", ".
# NOTE: On every operation, the starting set should be the odd set


odd_set = set()
even_set = set()
for _ in range(1, int(input())+1):
	name_asci = int(sum([ord(c) for c in input()]) / _)
	if name_asci % 2 == 0:
		even_set.add(name_asci)
	else:
		odd_set.add(name_asci)

if sum(odd_set) == sum(even_set):
	print(', '.join((map(str, odd_set.union(even_set)))))
elif sum(odd_set) > sum(even_set):
	print(', '.join(map(str, odd_set.difference(even_set))))
else:
	print(', '.join(map(str, odd_set.symmetric_difference(even_set))))

