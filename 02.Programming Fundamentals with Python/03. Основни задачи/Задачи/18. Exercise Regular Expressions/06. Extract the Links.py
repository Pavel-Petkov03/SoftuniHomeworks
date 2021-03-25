# Write a program that extracts links from a given text. The text will come in the form of strings, each representing a
# sentence. You need to extract only the valid links from it. Example:
import re
pattern = r'\www\.[A-Za-z0-9-]+(\.[a-z]+)+'
line = input()
while line:
	result = re.finditer(pattern, line)
	for c in result:
		if c.group():
			print(c.group())

	line = input()