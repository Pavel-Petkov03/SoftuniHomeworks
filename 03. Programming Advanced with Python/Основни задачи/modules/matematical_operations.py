

def get_result(first, symbol , second):
	if symbol == '^':
		symbol = '**'
	return f'{eval(f"{first}{symbol}{second}"):.2f}'

