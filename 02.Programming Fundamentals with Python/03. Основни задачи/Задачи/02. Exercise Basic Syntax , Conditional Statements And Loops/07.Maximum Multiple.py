import sys
max = -sys.maxsize
divisor = int(input())
bond = int(input())
for N in range(1, bond + 1):
    if N % divisor == 0:
        if N > max:
            max = N
print(max)