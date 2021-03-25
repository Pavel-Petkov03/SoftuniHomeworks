# Write program that:
# •	Reads an input string
# •	Reverses it using a stack
# •	Prints the result back on the console
c = [c for c in input()]
final = []
while c:
	final.append(c.pop())

print(''.join(final))


