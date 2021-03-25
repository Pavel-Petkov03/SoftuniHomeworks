import re
pattern = r'%(?P<name>[A-Z][a-z]+)%[^|$%.0-9]*<(?P<product>\w+)>[^|$%.0-9]*\|(?P<count>\d+)\|[^|$%.0-9]*(?P<price>\d+\.?\d+)\$'
command = input()
total_price = 0
while command != 'end of shift':
	result = re.finditer(pattern, command)
	for r in result:
		answer = r.groupdict()
		price = float(answer['price']) * int(answer['count'])
		print(f'{answer["name"]}: {answer["product"]} - {price:.2f}')
		total_price += price
	command = input()


print(f'Total income: {total_price:.2f}')
