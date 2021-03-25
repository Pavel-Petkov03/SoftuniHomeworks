# You are about to make some good money, but first you need to think of a way to verify who paid for your
# product and who didn`t. You have decided to let people use the software for a free trial period and then
# require an activation key in order to continue to use the product. The last step before you could cash out
# is to design a program that creates unique activation keys for each user. So, waste no more time and start typing!
#
# The first line of the input will be your raw activation key. It will consist of letters and numbers only.
# After that, until the "Generate" command is given, you will be receiving strings with instructions for
# different operations that need to be performed upon the raw activation key.
# There are several types of instructions, split by ">>>":
# •	Contains>>>{substring} – checks if the raw activation key contains the given substring.
# o	If it does prints: "{raw activation key} contains {substring}".
# o	If not, prints: "Substring not found!"
# •	Flip>>>Upper/Lower>>>{startIndex}>>>{endIndex}
# o	Changes the substring between the given indices (the end index is exclusive) to upper or lower case.
# o	All given indexes will be valid.
# o	Prints the activation key.
# •	Slice>>>{startIndex}>>>{endIndex}
# o	Deletes the characters between the start and end indices (end index is exclusive).
# o	Both indices will be valid.
# o	Prints the activation key.
# Input
# •	The first line of the input will be string and it will consist of letters and numbers only.
# •	After the first line, until the "Generate" command is given, you will be receiving strings.
# Output
# •	After the "Generate" command is received, print:
# o	"Your activation key is: {activation key}"

text= input()
command = input()
while command != 'Generate':
	c = command.split('>>>')
	if len(c) == 2:
		task, substring = c
		if task == 'Contains':
			if substring in text:
				print(f"{text} contains {substring}")
			else:
				print("Substring not found!")

	elif len(c) == 3:
		_ , start, end = c
		text = ''.join([text[c] for c in range(len(text)) if c < int(start) or c >= int(end)])
		print(text)
	elif len(c) == 4:
		_, u_l, start, end = c
		if _ == 'Flip':
			if u_l == 'Upper':
				text = [text[c].upper() if int(start) <= c < int(end) else text[c] for c in range(len(text))]
			elif u_l == 'Lower':
				text = [text[c].lower() if int(start) <= c < int(end) else text[c] for c in range(len(text))]

			text = ''.join(text)
			print(text)
	command = input()

print(f'Your activation key is: {text}')

