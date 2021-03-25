# Write a function called numbers_searching which receives a different
# amount of parameters. All parameters will be integer numbers forming a sequence of consecutive numbers.
# Your task is to find an unknown amount of duplicates from the given sequence and a missing value, such that
# all the duplicate values and the missing value are between the smallest and the biggest received number.
# The function should return a list with the last missing number as a first argument and a sorted list, containing
# the duplicates found, in ascending order.
# For example: if we have the following numbers: 1, 2, 4, 2, 5, 4 will return 3 as missing number and 2, 4 as
# duplicate numbers in the following format: [3, [2, 4]]
# Input
# •	There will be no input
# •	Parameters will be passed to your function
# Output
# •	The function should return a list in the following format: [missing number, [duplicate_numbers separated
# with comma and space]]
# Constraints
# •	The missing number will always be between the smallest and the biggest received number


def numbers_searching(*args):
    list_dup = list(set([c for c in args if args.count(c) >= 2]))
    args = list(sorted(args))
    miss = None
    for num in range(len(args)-1):
        if args[num] != args[num+1]:
            if args[num] + 1 != args[num+1]:
                miss = args[num]+1
                break

    return [miss, sorted(list_dup)]


print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
print(numbers_searching(1, 2, 4, 2, 5, 4))


