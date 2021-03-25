# Write a program that counts all characters in a string except for space (' ').
# Print all the occurrences in the following format:
# {char} -> {occurrences}
our_dict = {}
word = input()
for item in range(len(word)):
	if word[item] != " ":
		if word[item] in our_dict:
			our_dict[word[item]] += 1
		else:
			our_dict[word[item]] = 1


for key, value in our_dict.items():
	print(f'{key} -> {value}')

