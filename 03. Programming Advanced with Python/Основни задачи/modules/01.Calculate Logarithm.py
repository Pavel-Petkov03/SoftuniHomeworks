from math import log


def use_log(x, bace):
	if bace == 'natural':
		return f'{log(x):.2f}'
	else:
		return f'{log(x, int(bace)):.2f}'


print(use_log(int(input()), input()))




