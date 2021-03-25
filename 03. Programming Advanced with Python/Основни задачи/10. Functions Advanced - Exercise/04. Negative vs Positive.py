# You will receive a list of numbers. Separate the negative numbers from the positive.
# Find the total sum of the negatives and positives, replace the negative number with its
# absolute value and print the following:
# If the absolute negative number is bigger than the positive number:
# 	"The negatives are stronger than the positives"
# If the positive number is bigger than the absolute negative number:
# 	"The positives are stronger than the negatives"



def negative(m_list):
	return sum(filter(lambda x: x < 0, m_list))


def positive(m_list):
	return sum(filter(lambda x: x > 0, m_list))


my_list = list(map(int, input().split()))
print(negative(my_list))
print(positive(my_list))
if abs(negative(my_list)) > positive(my_list):
	print('The negatives are stronger than the positives')
else:
	print('The positives are stronger than the negatives')


