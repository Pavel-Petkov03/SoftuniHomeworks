# Every gamer knows what rage-quitting means. It’s basically when you’re just not good enough and you blame everybody
# else for losing a game. You press the CAPS LOCK key on the keyboard and flood the chat with gibberish to show your
# frustration.
# Chochko is a gamer, and a bad one at that. He asks for your help; he wants to be the most annoying kid in his team,
# so when he rage-quits he wants something truly spectacular. He’ll give you a series of strings followed
# by non-negative
# numbers, e.g. "a3"; you need to print on the console each string repeated N times; convert the letters to uppercase
# beforehand. In the example, you need to write back "AAA".
# On the output, print first a statistic of the number of unique symbols used (the casing of letters is irrelevant,
# 'A' are the same); the format shoud be "Unique symbols used {0}". Then, print the rage message itself.
# The strings and numbers will not be separated by anything. The input will always start with a string and for e
# ach string there will be a corresponding number. The entire input will be given on a single line; Chochko is
# too lazy to make your job easier.
# Input
# •	The input data should be read from the console.
# •	It consists of a single line holding a series of string-number sequences.
# •	The input data will always be valid and in the format described. There is no need to check it explicitly.
# Output
# •	The output should be printed on the console. It should consist of exactly two lines.
# •	On the first line, print the number of unique symbols used in the message.
# •	On the second line, print the resulting rage message itself.
# Constraints
word = input()
digit = ''
actual_word = ''
index = 0
current = ''
while index < len(word):
	if word[index].isdigit():
		while index < len(word) and word[index].isdigit():
			digit += word[index]
			index += 1
		actual_word += int(digit) * current.upper()
		digit = ''
		current = ''
	else:
		current += word[index]
		index += 1


print(f'Unique symbols used: {len(set(actual_word.upper()))}')
print(actual_word)

