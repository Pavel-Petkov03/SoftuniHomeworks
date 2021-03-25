# Write a program that rounds all the given numbers. Use round()

float_list = map(float, input().split())
def float_to_round(ll):
	return list(map(round , ll))



print(float_to_round(float_list))