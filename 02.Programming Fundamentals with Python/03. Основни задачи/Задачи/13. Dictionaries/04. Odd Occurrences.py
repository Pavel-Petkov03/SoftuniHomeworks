# Write a program that extracts all elements from a given sequence of words that are present
# in it an odd number of times (case-insensitive).
# �	Words are given on a single line, space separated.
# �	Print the result elements in lowercase, in their order of appearance.
our_dict = {}
our_list = input().split()
for item in our_list:
	if item.lower() not in our_dict:
		our_dict[item.lower()] = 1
	else:
		our_dict[item.lower()] += 1
for key,value in our_dict.items():
	if value % 2 != 0:
		print(key, end=" ")


