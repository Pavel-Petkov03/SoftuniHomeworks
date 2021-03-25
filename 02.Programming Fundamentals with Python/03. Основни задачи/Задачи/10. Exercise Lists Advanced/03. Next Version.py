# You're fed up about changing the version of your software manually. Instead, you will create a little script that
# will make it for you.
# You will be given a version as in this example: "1.3.4". You have to find the next version and print it
# ("1.3.5" from the example). The only rule is that the numbers cannot be greater than 9. If that happens,
# set the current number to 0 and increase the number before it. For more clarification, see the examples.
# Note: there will be no case where the first number will get greater than 9
def version(string):
	new_string = list(map(lambda x: int(x) , string.split(".")))
	new_string[2] += 1
	if new_string[2] > 9:
		new_string[2] = 0
		new_string[1] += 1
		if new_string[1] > 9:
			new_string[0] += 1
			new_string[1] = 0
	return f"{new_string[0]}.{new_string[1]}.{new_string[2]}"


our_string = input()
print(version(our_string))






