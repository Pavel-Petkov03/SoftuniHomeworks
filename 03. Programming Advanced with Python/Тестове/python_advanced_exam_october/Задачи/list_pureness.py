# Write function called best_list_pureness which will receive a list of numbers and a number K.
# You have to rotate the list K times (last becomes first) to find the variation of the list with t
# he best pureness (pureness is calculated by summing all the elements in the list multiplied by their indices).
# For example, in the list [4, 3, 2, 6] with the best pureness is (3 * 0) + (2 * 1) + (6 * 2) + (4 * 3) = 26. At
# the end the function should return a string containing the highest pureness and the amount of rotations that were made
# to find this pureness in the following format: "Best pureness {pureness_value} after {count_rotations} rotations".
# If there is more than one highest pureness, take the first one.
# Note: Submit only the function in the judge system
# Input
# •	There will be no input, just parameters passed to your function
# Output
# •	There is no expected output
# •	The function should return a string in the following format:
# "Best pureness {pureness_value} after {count_rotations} rotations"


from collections import deque


def best_list_pureness(*my_list):
    best_pureness = - 1
    best_rotation = None
    my_range = my_list[-1]
    my_list1 = deque(my_list[0].copy())
    for rotate in range(my_range + 1):
        current_rotation = sum([index * my_list1[index] for index in range(len(my_list1))])
        if current_rotation > best_pureness:
            best_pureness = current_rotation
            best_rotation = rotate
        my_list1.appendleft(my_list1.pop())

    return f'Best pureness {best_pureness} after {best_rotation} rotations'


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
