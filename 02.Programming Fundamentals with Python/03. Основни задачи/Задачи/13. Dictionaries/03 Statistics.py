# You seem to be doing great at your first job. You have now successfully completed the first 2 of your tasks and
# your boss decides to give you as your next task something more challenging. You have to accept all the new
# products coming in the bakery and finally gather some statistics.
# You will be receiving key-value pairs on separate lines separated by ": " until you receive the command
# "statistics". Sometimes you may receive a product more than once. In that case you have to add the new
# quantity to the existing one. When you receive the "statistics" command, print the following:
# "Products in stock:
# - {product1}: {quantity1}
# - {product2}: {quantity2}
# …
# Total Products: {count_all_products}
# Total Quantity: {sum_all_quantities}"
our_dict = {}
command = input()
counter = 0
while command != "statistics":
	key, value = command.split(": ")
	value = int(value)
	counter += value
	if key in our_dict:
		our_dict[key] += value
	else:
		our_dict[key] = int(value)
	command = input()
print('Products in stock:')
for items in our_dict:
	print(f'- {items}: {our_dict[items]}')
print(f'Total Products: {len(our_dict)}')
print(f'Total Quantity: {counter}')

