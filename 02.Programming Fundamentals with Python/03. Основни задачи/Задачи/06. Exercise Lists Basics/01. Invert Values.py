# Write a program that receives a single string containing numbers separated
# by a single space. Print a list containing the opposite of each number.
array = input().split()
print([-int(array[c]) for c in range(len(array))])