# Using a list comprehension, write a program that receives numbers,
# separated by comma and space ", ", and prints all the positive, negative, even and
# odd numbers on separate lines as shown below.
# Note: Zero is counted for a positive number


row = list(map(int, input().split(', ')))


def even(n):
	return n % 2 == 0


def odd(n):
	return n % 2 != 0


def negative(n):
	return n < 0


def positive(n):
	return n >= 0


def int_to_str(r):
	return ', '.join(list(map(str, r)))


print(f'Positive: {int_to_str([c for c in row if positive(c)])}')
print(f'Negative: {int_to_str([c for c in row if negative(c)])}')
print(f'Even: {int_to_str([c for c in row if even(c)])}')
print(f'Odd: {int_to_str([c for c in row if odd(c)])}')