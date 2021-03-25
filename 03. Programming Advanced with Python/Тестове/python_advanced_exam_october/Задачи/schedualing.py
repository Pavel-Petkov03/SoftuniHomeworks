# On the first line you will be given the jobs as integers (clock-cycles needed to finish the job)
# separated by comma and space ", ". On the second line you will be given the index of the job that we are
# interested in and want to know how many cycles will pass until the job is done.
# The tasks that need the least amount of clock-cycles will be completed first.
# For the jobs that need the same amount of clock-cycles, the order is FIFO (First In First Out).
# You have to print how many clock-cycles will pass until the task you are interested in is completed. For
# more clarifications, see the examples below.
# Input
# •	On the first line you will receive numbers separated by ", "
# •	On the second line you will receive the index of the task you are interested in


from collections import deque
array = deque(list(map(int, input().split(', '))))
place = int(input())
current = array[place]
final = 0
while current in array:
    min_clock = min(array)
    for _ in range(len(array)):
        if array[0] == min_clock:
            final += array.popleft()
            break
        array.append(array.popleft())

print(final)
