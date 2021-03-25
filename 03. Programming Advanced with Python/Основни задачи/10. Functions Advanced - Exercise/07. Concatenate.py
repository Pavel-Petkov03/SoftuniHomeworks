# Write a function called concatenate() that receives some strings, concatenates them and returns the result

def concatenate(*args):
	return ''.join(args)
print(concatenate("Soft", "Uni", "Is", "Great", "!"))