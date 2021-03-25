

# Write a program that returns an encrypted version of the same text. Encrypt the text by shifting each character
# with three positions forward. For example A would be replaced by D, B would become E, and so on. Print the
# encrypted text.


text = input()
new_word = ''

for index in range(len(text)):
	new_word += chr(ord(text[index]) + 3)

print(new_word)