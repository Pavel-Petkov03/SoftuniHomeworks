# Using a comprehension, write a program that receives some text, separated by space, and
# take only those words, whose length is even. Print each word on a new line.

def is_even(c):
	return len(c) % 2 == 0

my_list = input().split()
[print(c) for c in my_list if is_even(c)]