# Write a program that reads a matrix from the console and prints:
# •	The sum of all matrix elements
# •	The matrix itself
# On the first line, you will get matrix sizes in format "{rows}, {columns}"


row, col = map(int, input().split(', '))
matrix = [list(map(int , input().split(', '))) for c in range(row)]
print(sum([sum(c) for c in matrix]))
print(matrix)