# You will receive a single line containing numbers separated by a single space.
# Form the biggest number possible from them by sorting them as strings.
def reverse(string):
	return "".join(sorted(string.split(), reverse=True))
our_string = input()
print(reverse(our_string))