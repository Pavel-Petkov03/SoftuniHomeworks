# Write a program that receives a matrix and prints the flattened version of it (a list with all
# the values). For example, the flattened list of the matrix: [[1, 2], [3, 4]] will be [1, 2, 3, 4].

row = result = []
a = ([[result.append(d) for d in list(map(int, input().split(', ')))] for c in range(int(input()))])
print(result)