# You will be given series of strings until you receive an "end" command. Write a program that reverses strings and
# prints each pair on separate line in format "{word} = {reversed word}".

word = input()
while word != 'end':
	print(f'{word} = {word[::-1]}')
	word = input()
