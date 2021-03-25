# You will be given a start and an end. Print all the numbers in the given range (inclusive)
# that are divisible by any of the numbers from 2 to 10. Use comprehensions for this problem.

prompt = [c for c in range(2, 11)]
start, end = int(input()) , int(input())
a = list(set([c for d in prompt for c in range(start, end +1) if c % d == 0]))
print(a)




