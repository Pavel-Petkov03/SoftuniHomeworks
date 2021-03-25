# Write a program that receives a list of numbers. Print only the even numbers from the list. Use filter()

def even(my_list):
	return list(filter(lambda x : x % 2 == 0, my_list))


m_list = list(map(int , input().split()))
print(even(m_list))