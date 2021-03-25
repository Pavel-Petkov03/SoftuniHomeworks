# You have an empty sequence, and you will be given N queries. Each query is one of these three types:
# 1 – Push the element x into the stack.
# 2 – Delete the element present at the top of the stack.
# 3 – Print the maximum element in the stack.
# 4 – Print the minimum element in the stack.
# After you go through all the queries, print the stack in the following format:
# "{n}, {n1}, {n2} …, {nn}"
# Input
# •	The first line of input contains an integer, N
# •	The next N lines each contain an above-mentioned query. (It is guaranteed that each query is valid.)
# Output
# •	For each type 3 or 4 query, print the maximum/minimum element in the stack on a new line

stack = []
for c in range(int(input())):
	command = input().split()
	if command[0] == '1':
		stack.append(int(command[1]))
	elif command[0] == '2':
		if stack:
			stack.pop()
	elif command[0] == '3':
		if stack:
			print(max(stack))
	elif command[0] == '4':
		if stack:
			print(min(stack))
print(', '.join([str(c) for c in reversed(stack)]))
