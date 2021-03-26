# Write a function called list_manipulator which receives a list of numbers as
# first parameter and different amount of other parameters. The second parameter
# might be "add" or "remove". The third parameter might be "beginning" or "end".
# There might or might not be any other parameters (numbers):
# •	In case of "add" and "beginning", add the given numbers to the beginning of the
# given list of numbers and return the new list
# •	In case of "add" and "end", add the given numbers to the end of the given list of numbers and return the new list
# •	In case of "remove" and "beginning"
# o	If there is another parameter (number), remove that amount of numbers from the beginning of the list of numbers.
# o	If there are no other parameters, remove only the first element of the list.
# o	Finaly, return the new list
# •	In case of "remove" and "end"
# o	If there is another parameter (number), remove that amount of numbers from the end of the list of numbers.
# o	Otherwise if there are no other parameters, remove only the last element of the list.
# o	Finaly, return the new list
# For more clarifications, see the examples below.
# Input
# •	There will be no input
# •	Parameters will be passed to your function
# Output
# •	The function should return the new list of numbers


from collections import deque
def list_manipulator(*args):
    my_list = args[0]
    second_param = args[1]
    third_param = args[2]
    if second_param == 'remove':
        if third_param == 'beginning':
            my_list = deque(my_list)
            if len(args) == 4:
                forth_param = args[3]
                for r in range(forth_param):
                    my_list.popleft()
            else:
                my_list.popleft()
        elif third_param == 'end':
            if len(args) == 4:
                forth_param = args[3]
                for r in range(forth_param):
                    my_list.pop()
            else:
                my_list.pop()
    elif second_param == 'add':
        nums = args[3:]
        if third_param == 'beginning':
            my_list = deque(my_list)
            for n in reversed(nums):
                my_list.appendleft(n)
        elif third_param == 'end':
            for n in nums:
                my_list.append(n)

    return list(my_list)





print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
