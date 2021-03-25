# Write a program that reads a single string with numbers separated by comma and space ", ".
# Print the indices of all even numbers
def even(string):
	splited = string.split(", ")
	return [index for index in range(len(splited)) if int(splited[index]) % 2 == 0]

our_string = input()
print(even(our_string))
