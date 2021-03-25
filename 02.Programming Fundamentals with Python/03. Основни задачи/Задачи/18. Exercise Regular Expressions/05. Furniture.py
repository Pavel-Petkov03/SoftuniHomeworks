# Write a program to calculate the total cost of different types of furniture.
# You will be given some lines of input until you receive the line "Purchase".
# For the line to be valid it should be in the following format:
# ">>{furniture name}<<{price}!{quantity}"
# The price can be floating point number or whole number. Store the names of the
# furniture and the total price. At the end print the each bought furniture on separate line in the format:
# "Bought furniture:
# {1st name}
# {2nd name}
# …"
# And on the last line print the following: "Total money spend: {spend money}" formatted to the second decimal point.

import re
command = input()
filtered = []
pattern = r'>>(?P<furniture>[A-Za-z]+)<<(?P<float_price>\d+\.?\d+)!(?P<quantity>\d+)'
while command != 'Purchase':
	filtered.append(re.finditer(pattern, command))
	command = input()
print('Bought furniture:')
total = 0
for index in filtered:
	for i in index:
		needed = i.groupdict()
		print(needed['furniture'])
		total += float(needed['float_price']) * int(needed['quantity'])
print(f'Total money spend: {total:.2f}')
