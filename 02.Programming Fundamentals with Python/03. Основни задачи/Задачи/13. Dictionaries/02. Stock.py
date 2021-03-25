# After you have successfully completed your first task, your boss decides to give you another one right away.
# Now not only you have to keep track of the stock, but also you have to answer customers
# if you have some products in stock or not.
# You will be given key-value pairs of products and quantities (on a single line separated by space).
# On the next line you will be given products to search for. Check for each product, you have 2 possibilities:
# •	If you have the product, print "We have {quantity} of {product} left"
# •	Otherwise, print "Sorry, we don't have {product}"
listed = input().split()
our_dict = {}
for times in range(0, len(listed), 2):
	key = listed[times]
	value = int(listed[times + 1])
	our_dict[key] = value

our_list = input().split()
for key in our_list:
	if key in our_dict:
		print(f"We have {our_dict.get(key)} of {key} left")
	else:
		print(f"Sorry, we don't have {key}")

