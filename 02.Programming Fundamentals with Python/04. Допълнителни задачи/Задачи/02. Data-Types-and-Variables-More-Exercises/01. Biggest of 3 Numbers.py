# Write a program that finds the biggest of 3 numbers.
# The input comes as 3 integers.
# The output is the biggest from the input numbers.
first = int(input())
second = int(input())
third = int(input())
if first > second and first > third:
    print(first)
elif second > third and second > first:
    print(second)
else:
    print(third)