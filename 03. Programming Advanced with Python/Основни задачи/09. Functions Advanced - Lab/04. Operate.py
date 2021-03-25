# Write a function called multiply that can receive any amount of numbers as different parameters and returns
# the result of the multiplication of all of them. Submit only your function in judge.

from functools import reduce
def operate(operator , *args):
	return reduce(lambda x , y: eval(f'{x} {operator} {y}'), args)



print(operate("+", 1, 2, 3))
