# Write a program that prints you a receipt for your new computer.
# You will receive the prices (without tax) of the parts until you receive what type of customer
# is this - special or regular. Once you receive the type of the customer you should print the receipt.
# The taxes are 20% of each part's price you receive.
# If the customer is special, then he has a 10% discount of the price of the total price with taxes.
# If a given price is not positive number, you should print "Invalid price!"
# on the console and continue with the next price.
# If total price is equal to zero, you should print "Invalid order!" on the console.
# Input
# �	You will receive numbers representing prices (without tax) until command "special" or "regular":
# Output
# �	The receipt should be in the following format:
#
# "Congratulations you've just bought a new computer!
# Price without taxes: {total price without taxes}$
# Taxes: {total amount of taxes}$
#
# Total price: {total price with taxes}$"

command = input()
sum_ = 0
while command != "regular" and command != "special":
	tax = float(command)
	if tax < 0:
		print("Invalid price!")
		command = input()
		continue
	sum_ += tax
	command = input()

if sum_ == 0:
	print("Invalid order!" )
else:
	print("Congratulations you've just bought a new computer!")
	print(f'Price without taxes: {sum_:.2f}$')
	print(f'Taxes: {(sum_*0.2):.2f}$')
	print('-----------')
	sum_ += sum_ * 0.2
	if command == "special":
		sum_ *= 0.9
	print(f'Total price: {sum_:.2f}$')





