# Write a Program That Reads a list of strings. Each string is repeated N times,
# where N is the length of the string. Print the concatenated string.
result = ''
word = input().split()
for index in range(len(word)):
	result += len(word[index]) * word[index]

print(result)