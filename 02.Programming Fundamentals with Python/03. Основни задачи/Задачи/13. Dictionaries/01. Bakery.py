# This is your first task in your new job. You were tasked to create a list of the stock in a bakery and
# you really don't want to fail at you first day at work.
# You will receive a single line containing some food (keys) and quantities (values).
# They will be separated by a single space (the first element is the key, the second – the value and so on).
# Create a dictionary with all the keys and values and print it on the console

listed_bakery = input().split()
bakery = {}
for times in range(0,len(listed_bakery), 2):
	key = listed_bakery[times]
	value = int(listed_bakery[times + 1])
	bakery[key] = value

print(bakery)