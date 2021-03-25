# '''
# Write a program that reads N integers from the console and reverses them using a stack
# '''
old = [c for c in input().split()]
stack = []
while old:
	stack.append(old.pop())

print(' '.join(stack))