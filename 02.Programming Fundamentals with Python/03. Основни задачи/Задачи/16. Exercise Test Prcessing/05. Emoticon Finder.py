# Find all emoticons in the text. An emoticon always starts with ":" and is followed by a symbol.
# The input will be provided as a single string.

text = input()
for index in range(len(text)):
	if text[index] == ":":
		print(f':{text[index + 1]}')
		