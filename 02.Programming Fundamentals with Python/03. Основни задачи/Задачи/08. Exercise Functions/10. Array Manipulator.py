# Trifon has finally become a junior developer and has received his first task. It's about manipulating an array of
# integers. He is not quite happy about it, since he hates manipulating arrays. They are going to pay him a lot of money
# , though, and he is willing to give somebody half of it if to help him do his job. You, on the other hand, love arrays
# (and money) so you decide to try your luck.
# The array may be manipulated by one of the following commands
# ?	exchange {index} ? splits the array after the given index, and exchanges the places of the two resulting
# sub-arrays. E.g. [1, 2, 3, 4, 5] -> exchange 2 -> result: [4, 5, 1, 2, 3]
# o	If the index is outside the boundaries of the array, print "Invalid index"
# ?	max even/odd? returns the INDEX of the max even/odd element -> [1, 4, 8, 2, 3] -> max odd -> print 4
# ?	min even/odd ? returns the INDEX of the min even/odd element -> [1, 4, 8, 2, 3] -> min even > print 3
# o	If there are two or more equal min/max elements, return the index of the rightmost one
# o	If a min/max even/odd element cannot be found, print "No matches"
# ?	first {count} even/odd? returns the first {count} elements -> [1, 8, 2, 3] -> first 2 even -> print [8, 2]
# ?	last {count} even/odd ? returns the last {count} elements -> [1, 8, 2, 3] -> last 2 odd -> print [1, 3]
# o	If the count is greater than the array length, print "Invalid count"
# o	If there are not enough elements to satisfy the count, print as many as you can. If there are zero even/odd
# elements, print an empty array "[]"
# ?	end ? stop taking input and print the final state of the array
# Input
# ?	The input data should be read from the console.
# ?	On the first line, the initial array is received as a line of integers, separated by a single space
# ?	On the next lines, until the command "end" is received, you will receive the array manipulation commands
# ?	The input data will always be valid and in the format described. There is no need to check it explicitly.
# Output
# ?	The output should be printed on the console.
# ?	On a separate line, print the output of the corresponding command
# ?	On the last line, print the final array in square brackets with its elements separated by a comma and a space
# ?	See the examples below to get a better understanding of your task
# Constraints
# ?	The number of input lines will be in the range [2 ? 50].
# ?	The array elements will be integers in the range [0 ? 1000].
# ?	The number of elements will be in the range [1 .. 50]
# ?	The split index will be an integer in the range [-231 ? 231 ? 1]
# ?	first/last count will be an integer in the range [1 ? 231 ? 1]
# ?	There will not be redundant whitespace anywhere in the input
# # ?	Allowed working time for your program: 0.1 seconds. Allowed memory: 16 MB.
import sys
def array_manipulator(array):

    def exchange(task_array, index):
        index = int(index)
        return array[index + 1:] + array[:index + 1]

    def max_num(task_array , odd_or_even):
        our_max_num = -sys.maxsize
        is_found = False
        wanted_index = None
        if odd_or_even == "even":
            for index in range(len(task_array)):
                if int(task_array[index]) % 2== 0 and our_max_num <= int(task_array[index]):
                    is_found = True
                    our_max_num = task_array[index]
                    wanted_index = index
        elif odd_or_even == "odd":
            for index in range(len(task_array)):
                if int(task_array[index]) % 2 != 0 and our_max_num <= int(task_array[index]):
                    is_found = True
                    our_max_num = task_array[index]
                    wanted_index = index
        if not is_found:
            return "No matches"
        return wanted_index

    def min_num(task_array , odd_or_even):
        our_min_num = sys.maxsize
        wanted_index = None
        is_found = False
        if odd_or_even == "even":
            for index in range(len(task_array)):
                if task_array[index] % 2 == 0 and int(task_array[index]) <= our_min_num:
                    is_found = True
                    our_min_num = task_array[index]
                    wanted_index = index
        elif odd_or_even == "odd":
            for index in range(len(task_array)):
                if task_array[index] % 2 != 0 and int(task_array[index]) <= our_min_num:
                    is_found = True
                    our_min_num = task_array[index]
                    wanted_index = index
        if not is_found:
            return "No matches"
        return wanted_index

    def first_count(array, count, even_or_odd):
        count = int( count )
        if len(array) < count:
            return 'Invalid count'
        if even_or_odd == 'even':
            all_nums = [i for i in array if i % 2 == 0]
            if len( all_nums ) < count:
                return all_nums
            elif len( all_nums ) == 0:
                return []
            else:
                return all_nums[:count]

        elif even_or_odd == 'odd':
            all_nums = [i for i in array if i % 2 != 0]
            if len( all_nums ) < count:
                return all_nums
            elif len(all_nums ) == 0:
                return []
            else:
                return all_nums[:count]

    def last_count(array, count, even_or_odd):
        count = int( count )
        if len(array) < count:
            return 'Invalid count'
        if even_or_odd == 'even':
            all_nums = [i for i in array if i % 2 == 0]
            if len( all_nums) < count:
                return all_nums
            elif len( all_nums ) == 0:
                return []
            else:
                return all_nums[len(all_nums) - count:]

        elif even_or_odd == 'odd':
            all_nums = [i for i in array if i % 2 != 0]
            if len( all_nums ) < count:
                return all_nums
            elif len( all_nums ) == 0:
                return []
            else:
                return all_nums[len(all_nums) - count:]

    array = [int(array.split()[c]) for c in range(len(array.split()))]
    command = input()
    while command != "end":
        actual_command = command.split()
        if actual_command[0] == "exchange":
            if 0 <= int(actual_command[1]) < len(array):
                array = exchange( array, actual_command[1] )
            else:
                print( "Invalid index" )
        elif actual_command[0] == "max":
            print(max_num(array, actual_command[1]))
        elif actual_command[0] == "min":
            print(min_num(array, actual_command[1]))
        elif actual_command[0] == "first":
            print(first_count(array, actual_command[1], actual_command[2]))
        elif actual_command[0] == "last":
            print(last_count(array, actual_command[1], actual_command[2]))
        command = input()
    return array


our_array = input()
print(array_manipulator(our_array))


        



