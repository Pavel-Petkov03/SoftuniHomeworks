# Write a program that reads a single string and prints all the possible
# combinations of the characters in that string. Submit your solution in the judge system.

names = input().split(', ')
count = int(input())


def combinations(my_names, my_count, temp=[]):
	if len(temp) == my_count:
		print(temp)
		return
	for i in range(len(my_names)):
		name = my_names[i]
		temp.append(name)
		combinations(my_names[i + 1:], my_count, temp)
		temp.pop()


combinations(names, count)
