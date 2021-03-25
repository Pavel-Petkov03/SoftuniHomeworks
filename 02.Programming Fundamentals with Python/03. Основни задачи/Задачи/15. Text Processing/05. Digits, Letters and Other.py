# Write a program that receives a single string and on the first line prints all the digits, on the second –
# all the letters, and on the third – all the other characters. There
# will always be at least one digit, one letter and one other characters.

alphas = ''
digits = ''
else_symbols = ''
text = input()
for char in text:
	if char.isdigit():
		digits += char
	elif char.isalpha():
		alphas += char
	else:
		else_symbols += char

print(digits)
print(alphas)
print(else_symbols)



