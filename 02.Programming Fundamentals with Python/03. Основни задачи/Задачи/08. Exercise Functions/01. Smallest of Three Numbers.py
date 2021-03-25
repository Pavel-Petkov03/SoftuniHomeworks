# Write a function which receives three integer numbers and returns the smallest.
# Use appropriate name for the function.
def smaller(a,b,c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c


first = int(input())
second = int(input())
third = int(input())
print(smaller(first, second, third))

