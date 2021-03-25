# Write a program that finds the sum of matrix primary diagonal

n = int(input())
matrix = [list(map(int, input().split())) for c in range(n)]
counter = 0
sum_ = 0
for c in range(n):
	sum_ += matrix[c][c]
print(sum_)
