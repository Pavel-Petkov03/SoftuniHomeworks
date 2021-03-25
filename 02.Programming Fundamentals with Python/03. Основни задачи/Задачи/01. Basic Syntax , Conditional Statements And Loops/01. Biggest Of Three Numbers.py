first = int(input())
second = int(input())
third = int(input())
if first > second and first > third:
    print(first)
elif second > first and second > third:
    print(second)
else:
    print(third)

