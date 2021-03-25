# Your task is to write program which extracts emojis from a text and find the threshold based on the input.
# You have to get your cool threshold. It is obtained by multiplying all the digits found in the input.
# The cool threshold could be a very big number, so be mindful.
# An emoji is valid when:
# •	Is surrounded by either :: or ** (exactly 2)
# •	Is at least 3 characters long (without the surrounding symbols)
# •	Starts with a capital letter
# •	Continues with lowercase letters only
# Examples of valid emojis: ::Joy::, **Banana**, ::Wink::
# Examples of invalid emojis: ::Joy**, ::fox:es:, **Monk3ys**, :Snak::Es::
# You need to count all valid emojis in the text and calculate their coolness. The coolness of the emoji is determined
# by summing all the ASCII values of all letters in the emoji.
# Examples: ::Joy:: - 306, **Banana** - 577, ::Wink:: - 409
# You need to print the result of cool threshold and after that to take all emojis out of the text, count
# them and print the only the cool ones on the console.
# Input
# •	On the single input you will receive a piece of string.
# Output
# •	On the first line of the output print the obtained Cool threshold in format:
# •	Cool threshold: {coolThresholdSum}
# On the next line print the count of all emojis found in the text in format:
# •	{countOfAllEmojis} emojis found in the text. The cool ones are:
# •	{cool emoji 1}
# •	{cool emoji 2}
# •	{…}
# If there are no cool ones, just don't print anything in the end.
# Constraints
# There will always be at least one digit in the text!
import re
pattern_name = r'([:*])\1(?P<name>([A-Z][a-z]{2,}))\1\1'
text = input()
our_list = []
average_p = [int(c.group()) for c in re.finditer('\d' ,text )]
average = 1
for z in average_p:
	average*= z
em = []
for c in re.finditer(pattern_name , text):
	b = c.groupdict()
	initial_p = sum([ord(p) for p in b['name']])
	em.append(c.group())
	if initial_p > average:
		our_list.append(c.group())


if len(em) == 0:
	pass
else:
	print(f'Cool threshold: {average}')
	print(f'{len(em)} emojis found in the text. The cool ones are:')
	for i in our_list:
		print(i)

