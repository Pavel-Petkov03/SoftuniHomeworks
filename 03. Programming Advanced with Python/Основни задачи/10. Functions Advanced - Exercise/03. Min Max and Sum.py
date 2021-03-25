# Write a program that prints the min and max values from a list and the sum of
# all the numbers in the list. Use min(), max() and sum()
nums = list(map(int, input().split()))
print(f'The minimum number is {min(nums)}')
print(f'The maximum number is {max(nums)}')
print(f'The sum number is: {sum(nums)}')
