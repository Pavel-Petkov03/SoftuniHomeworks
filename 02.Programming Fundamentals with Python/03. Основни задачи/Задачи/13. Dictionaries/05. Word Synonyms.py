# Write a program, which keeps a dictionary with synonyms. The key of the dictionary will be the word.
# The value will be a list of all the synonyms of that word. You will be given a number n – the count of the words.
# After each word, you will be given a synonym, so the count of lines you have to read from the console is 2 * n.
# You will be receiving a word and a synonym each on a separate line like this:
# •	{word}
# •	{synonym}
# If you get the same word twice, just add the new synonym to the list.
# Print the words in the following format:
# {word} - {synonym1, synonym2… synonymN}
my_dict = {}
n = int(input())
for item in range(n):
	word = input()
	value = input()
	if word in my_dict:
		my_dict[word].append(value)
	else:
		my_dict[word] = [value]

for key, value in my_dict.items():
	print(f'{key} - {", ".join(value)}')

