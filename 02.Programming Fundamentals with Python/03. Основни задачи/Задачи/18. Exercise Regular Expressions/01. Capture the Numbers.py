# Write a program that finds all numbers in a sequence of strings.
# The output is all the numbers, extracted and printed on a single line – each separated by a single space.
import re
pattern = r'\d+'
line = input()
final = []
while line != '':
	nums = re.findall(pattern, line)
	if nums:
		final.extend(nums)
	line = input()

print(" ".join(final))