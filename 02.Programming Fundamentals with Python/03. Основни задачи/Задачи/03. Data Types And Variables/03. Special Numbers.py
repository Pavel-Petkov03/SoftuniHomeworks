# A number is special when the sum of its digits is 5, 7 or 11.
# Write a program to read an integer n and for all numbers in the range 1…n, print the number and if it is special
# or not (True / False).
n = int(input())
for num in range(1, n + 1):
    result = 0
    num_as_string = str(num)
    for index in num_as_string:
        result += int(index)
    if result == 7 or result == 11 or result == 5:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")


