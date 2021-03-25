# Write a program to flatten several lists of numbers, received in the following format:
# 	String with numbers separated by '|'.
# 	Values are separated by spaces (' ', one or several)
# 	Order the output list from the last to the first received, and their values from left to right as shown below.

my_text = input()
my_list = list(reversed(my_text.split('|')))
print(' '.join([num.strip() for nums in my_list for num in nums.split()]))

