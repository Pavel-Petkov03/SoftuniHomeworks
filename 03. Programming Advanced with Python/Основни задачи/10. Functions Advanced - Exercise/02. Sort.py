# Write a program that prints a sorted list of numbers in ascending order. Use sorted()

def sorting(my_words):
	return sorted(my_words)


m_word = list(map(int , input().split()))
print(sorting(m_word))