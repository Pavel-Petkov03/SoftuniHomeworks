# Write a program that decrypts a message by a given key and gathers information about hidden treasure
# type and its coordinates. On the first line you will receive a key (sequence of numbers). On the next few l
# ines until you receive "find" you will get lines of strings. You have to loop through every string and decrease
# the ascii code of each character with a corresponding number of the key sequence. The way you choose a key number
# from the sequence is just looping through it. If the length of the key sequence is less than the string sequence,
# you start looping from the beginning of the key. For more clarification see the example below. After decrypting the
# message you will get a type of treasure and its coordinates. The type will be between the symbol '&' and the
# coordinates will be between the symbols '<' and '>'. For each line print the type and the coordinates in format
# "Found {type} at {coordinates}".
array = [int(c) for c in input().split()]
command = input()
while command != 'find':
	index = 0
	result = ''
	for c in range(len(command)):
		if index == len(array):
			index = 0
		result += f'{chr(ord(command[c]) - array[index])}'

		index += 1
	final = [c for c in result]

	material = final[final.index('&')+1:final.index('&', final.index('&')+1)]
	coordinate = final[final.index('<')+1:final.index('>')]
	print(f'Found {"".join(material)} at {"".join(coordinate)}')
	command = input()
