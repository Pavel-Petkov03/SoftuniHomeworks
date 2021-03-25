# Write a program that receives a matrix of numbers and prints a new one only
# with the numbers that are even. Use nested comprehension for that problem.

print([[d for d in list(map(int, input().split(', '))) if d % 2 == 0] for c in range(int(input()))])
