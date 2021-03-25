# Write a program that receives a list of numbers and prints their absolute value. Use abs()


float_list = map(float, input().split())
def float_to_abs(ll):
	return list(map(abs, ll))



print(float_to_abs(float_list))

