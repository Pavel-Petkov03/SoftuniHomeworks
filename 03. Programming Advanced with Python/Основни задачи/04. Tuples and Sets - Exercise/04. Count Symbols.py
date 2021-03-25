# Write a program that reads a text from the console and counts the occurrences of each
# character in it. Print the results in alphabetical (lexicographical) order.

my_dict = {}
for c in input():
	if c not in my_dict:
		my_dict[c] = 0
	my_dict[c] += 1
for key, value in sorted(my_dict.items(), key =lambda x: x[0]):
	print(f'{key}: {value} time/s')

