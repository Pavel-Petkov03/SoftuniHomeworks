# Given two lists of strings print a new list of the strings that contains
# words from the first list which are substrings of any of the strings
# in the second list (only unique values)
# Input
# There will be 2 lines of input: the two lists separated by ", "

def contains(first_str , second_str):
	first_str = first_str.split(", ")
	return [first_str[item] for item in range(len(first_str)) if first_str[item] in second_str]

our_first = input()
our_second = input()
print(contains(our_first , our_second))
