# Write a program that keeps information about products and their prices. Each product has a name, a price and
# a quantity. If the product doesn't exist yet, add it with its starting quantity.
# If you receive a product, which already exists, increase its quantity by the input quantity and if its price
# is different, replace the price as well.
# You will receive products' names, prices and quantities on new lines. Until you receive the command "buy",
# keep adding items. When you do receive the command "buy", print the items with their names and total price
# of all the products with that name.
# Input
# •	Until you receive "buy", the products will be coming in the format: "{name} {price} {quantity}".
# •	The product data is always delimited by a single space.
# Output
# •	Print information about each product in the following format:
# "{productName} -> {totalPrice}"
# •	Format the average grade to the 2nd digit after the decimal separator

our_dict = {}
including_list = []
command = input()
while command != "buy":
	key, price, quantity = command.split()
	price = float(price)
	quantity = int(quantity)
	including_list = [price, quantity]
	if key in our_dict:
		our_dict[key][0] = price
		our_dict[key][1] += quantity
	else:
		our_dict[key] = including_list
	command = input()


for key, price_and_quantity in our_dict.items():
	price, quantity = price_and_quantity
	total = price * quantity
	print(f"{key} -> {total:.2f}")
