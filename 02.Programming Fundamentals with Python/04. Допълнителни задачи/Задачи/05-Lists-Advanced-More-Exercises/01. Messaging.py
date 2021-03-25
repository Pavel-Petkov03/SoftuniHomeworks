# You will be given a list of numbers and a string. For each element of the list you have to calculate the
# sum of its digits and take the element, corresponding to that index from the text. If the index is greater
# than the length of the text, start counting from the beginning (so that you always have a valid index).
# Then you get that element from the text, you must remove the character you have taken from it (so for the
# next index, the text will be with one character less).
def massage(num_list, string):
	num_list = list(map(lambda x: x, num_list.split()))
	result = ''
	for text in num_list:
		sum_ = 0
		for index in range(len(text)):
			sum_ += int(text[index])
		while len(string) <= sum_:
			sum_ -= len(string)
		result += string[sum_]
		first = string[:sum_]
		last = string[sum_ + 1:]
		string = first + last

	return result


our_list = input()
our_str = input()
print(massage(our_list, our_str))


