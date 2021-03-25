# Write a program that receives two numbers (factor and count) and creates
# a list with length of the given count and contains only elements that are multiples of the given factor.
a = []
divider=int(input())
n = int(input())
for i in range(0,(n + 1) * divider , divider):
    if i == 0:
        pass
    else:
        a.append(i)
print(a)
