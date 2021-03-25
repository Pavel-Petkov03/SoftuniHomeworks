# Explosions are marked with '>'. Immediately after the mark, there will be an integer, which
# signifies the strength of the explosion.
# You should remove x characters (where x is the strength of the explosion), starting after the punch character ('>').
# If you find another explosion mark ('>') while you’re deleting characters, you should
# add the strength to your previous explosion.
# When all characters are processed, print the string without the deleted characters.
# You should not delete the explosion character – '>', but you should delete the integers, which represent the strength.
# Input
# You will receive single line with the string.
# Output
# Print what is left from the string after explosions.
# Constraints
# •	You will always receive a strength for the punches
# •	The path will consist only of letters from the Latin alphabet, integers and the char '>'
# •	The strength of the punches will be in the interval [0…9]

text = input()
result = ''
strength = 0
for index in range(len(text)):
	if text[index] == '>':
		strength += int(text[index + 1])
		result += text[index]
	elif strength != 0:
		strength -= 1
	else:
		result += text[index]

print(result)