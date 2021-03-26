# You have plenty of free time, so you decide to write a program that conceals and reveals your received messages. Go ahead and type it in!
# On the first line of the input you will receive the concealed message. After that, until the "Reveal" command is given, you will be receiving strings with instructions for different operations that need to be performed upon the concealed message in order to interpret it and reveal its true content. There are several types of instructions, split by ":|:"
# •	InsertSpace:|:{index}
# o	Inserts a single empty space at the given index. The given index will always be valid.
# •	Reverse:|:{substring}
# o	If the message contains the given substring, cut it out, reverse it and add it at the end of the message.
# o	If not, print "error".
# o	This operation should replace only the first occurrence of the given substring if there are more than one such occurrences.
# •	ChangeAll:|:{substring}:|:{replacement}
# o	Changes all occurrences of the given substring with the replacement text.
# Input / Constraints
# •	On the first line, you will receive a string with message.
# •	On the next lines, you will be receiving commands, split by ":|:".
# Output
# •	After each set of instructions, print the resulting string.
# •	After the "Reveal" command is received, print this message:
# "You have a new text message: {message}"

text = input()
command = input()
while command != 'Reveal':
	if len(command.split(":|:")) != 3:
		c, doing = command.split(":|:")
		if c == 'InsertSpace':
			text = [c for c in text]
			text.insert(int(doing), ' ')
			text = ''.join(text)
			print(text)
		elif c == 'Reverse':
			if doing in text:
				text = text.replace(doing, '', 1)
				text = ([c for c in text])
				text.append(doing[::-1])
				text = ''.join(text)
				print(text)
			else:
				print('error')
	else:
		_, substring, replacement = command.split(":|:")
		text = text.replace(substring, replacement)
		print(text)

	command = input()

print(f"You have a new text message: {text}")
