# You are a mathematician during world war 2, who has joined the cryptography team to decipher the enemy's enigma code.
# Your job is to create a program to crack the codes.
# On the first line of the input you will receive the encrypted message. After that, until the "Decode" command is
# given, you will be receiving strings with instructions for different operations that need to be performed upon the
# concealed message to interpret it and reveal its true content. There are several types of instructions, split by '|'
# •	Move {number of letters}
# o	Moves the first n letters to the back of the string.
# •	Insert {index} {value}
# o	Inserts the given value before the given index in the string.
# •	ChangeAll {substring} {replacement}
# o	Changes all occurrences of the given substring with the replacement text.
# Input / Constraints
# •	On the first line, you will receive a string with message.
# •	On the next lines, you will be receiving commands, split by '|' .
# Output
# •	After the "Decode" command is received, print this message:
# "The decrypted message is: {message}"

our_str = input()
command = input()
while command != 'Decode':
	command = command.split("|")
	if command[0] == 'Move':
		_, place = command
		place = int(place)
		our_str = [c for c in our_str]
		our_str = ''.join(our_str[place:] + our_str[:place])

	elif command[0] == 'Insert':
		_, index , value = command
		our_str = [c for c in our_str]
		our_str.insert(int(index) , value)
		our_str = ''.join(our_str)

	elif command[0] == 'ChangeAll':
		_, old, new = command
		our_str = our_str.replace(old , new)
	command = input()

print(f'The decrypted message is: {our_str}')



