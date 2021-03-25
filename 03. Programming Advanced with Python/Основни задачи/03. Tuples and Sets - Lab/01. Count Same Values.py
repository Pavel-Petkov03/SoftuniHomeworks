# You will be given a list of numbers. Write a program that prints the number of occurrences of each number.
a = map(float , input().split())
values_dict = {}
for value in a:
	if value not in values_dict:
		values_dict[value] = 0
	values_dict[value] += 1

for key , value in values_dict.items():
	print(f'{key} - {value} times')
