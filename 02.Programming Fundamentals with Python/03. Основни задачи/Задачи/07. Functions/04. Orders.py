# Write a function that calculates the total price of an order and prints it on
# he console. The function should receive one of the following products: coffee,
# coke, water, snacks; and a quantity of the product. The prices for a single piece o
# f each product are:
# •	coffee - 1.50
# •	water - 1.00
# •	coke - 1.40
# •	snacks - 2.00
# Print the result formatted to the second decimal place.
def market(product , times):
    price = 0
    if product == "coffee":
        price = 1.5
    elif product == "water":
        price = 1
    elif product == "coke":
        price = 1.4
    elif product == "snacks":
        price = 2
    all_price = f'{(times * price):.2f}'
    return  all_price


needed_product = input()
needed_times = int(input())
print(market(needed_product , needed_times))

