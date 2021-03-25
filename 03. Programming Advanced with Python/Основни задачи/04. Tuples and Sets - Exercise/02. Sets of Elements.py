# Write a program that prints a set of elements.
# On the first line, you will receive two numbers - n and m, which represent the
# lengths of two separate sets. On the next n + m lines you will receive n numbers,
# which are the numbers in the first set, and m numbers, which are in the second set.
# Find all the unique elements that appear in both and print them on separate lines (the order does not matter).
# For example:
# Set with length n = 4: {1, 3, 5, 7}
# Set with length m = 3: {3, 4, 5}
# Set that contains all the elements that repeat in both sets -> {3, 5}



first, second = tuple(map(int, input().split()))
first_set = {input() for _ in range(first)}
second_set = {input() for _ in range(second)}
print('\n'.join((map(str, first_set.intersection(second_set)))))
