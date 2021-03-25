# Using a comprehension, write a program that finds the number of given items in a bunker and their average quality.
# On the first line, you will be given all item categories present in the bunker, then you will be given a number
# (n). On the next "n" lines, you will be given different items in the following format:
# "{category} - {item_name} - quantity:{item_quantity};quality:{item_quality}"
# Store that information, you will need it later. After you receive all the inputs, print the
# total amount of items (sum the quantities) in the format:
# "Count of items: {count}"
# After that, print the average quality of all items in the following format, formatted to the second digit:
# "Average quality: {quality sum/categories count}"
# Finally, print all categories with the items on separate lines in the format:
# "{category} -> {item1}, {item2}, …".


categories = {c:[] for c in input().split(', ')}

average = 0
count = 0

for _ in range(int(input())):
	category, item, quantity_and_quality = input().split(' - ')
	quantity, quality = quantity_and_quality.split(";")
	average += int(quality.split(":")[1])
	count += int(quantity.split(":")[1])
	categories[category].append(item)


print(f'Count of items: {count}')
print(f'Average quality: {(average / len(categories)):.2f}')
for key, value in categories.items():
	print(f'{key} -> {", ".join(categories[key])}')

