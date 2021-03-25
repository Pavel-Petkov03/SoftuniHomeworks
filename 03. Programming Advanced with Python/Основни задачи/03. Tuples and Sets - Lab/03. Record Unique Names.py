# Write a program, which will take a list of names and print only the unique names in the list.
# The order in which we print the result does not matter.

my_set = set()
for c in range(int(input())):
	a = input()
	my_set.add(a)
print("\n".join(my_set))