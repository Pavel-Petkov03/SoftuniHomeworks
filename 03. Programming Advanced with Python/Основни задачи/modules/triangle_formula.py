def fill(z):
	my_list = []
	for num in range(1,z+1):
		my_list.append(num)
	print(' '.join(list(map(str, my_list))))


def triangle(num):
	for index in range(1, num+1):
		fill(index)
	for index in range(num - 1, 0, -1):
		fill(index)
