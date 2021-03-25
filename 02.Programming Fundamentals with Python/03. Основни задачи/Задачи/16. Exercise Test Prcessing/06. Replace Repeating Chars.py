#  Write a program that reads a string from the console and replaces any sequence of the same letters with a single
#  corresponding letter.
word = input()
previous = word
index = 0
actual_word = ''
while index < len(word) - 1:
	if word[index] == word[index + 1]:
		pass
	else:
		actual_word += word[index]

	index += 1

print(actual_word + word[-1])
word = input()

