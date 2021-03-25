from math import ceil
budget = float(input())
students = int(input())
price_for_flour = float(input())
price_for_egg = float(input())
price_for_apron = float(input())
my = price_for_apron * ceil(1.2*students) + price_for_egg * 10 * students + price_for_flour * (students - students // 5)
if budget >= my:
	print(f'Items purchased for {my:.2f}$.')

else:
	print(f'{(my-budget):.2f}$ more needed.')


