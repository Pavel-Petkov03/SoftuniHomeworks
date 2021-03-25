# Write a program that receives a list of integer numbers and a number n. The number n represents the amount of
# numbers to remove from the list. You should remove the smallest ones.
# Input
# On the first line you will receive a string (numbers separated by a space), on the second
# line you will receive a number n (count of numbers to remove).
# Output
# Print all the numbers that are left in the list.
my_list = input().split()
exclude = int(input())
new_list = []
for c in range(len(my_list)):
    new_list.append(int(my_list[c]))
ascending_list = new_list.copy()
ascending_list.sort()
for out in range(exclude):
    new_list.remove(ascending_list[out])
print(new_list)


