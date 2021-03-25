# Write a function that receives two integer numbers. Calculate factorial of each
# number. Divide the first result by the
# second and print the division formatted to the second decimal point.
def big_division(a , b):
    div_a = 1
    div_b = 1
    for index in range(a , 1, -1):
        div_a *= index
    for index in range(b , 1, -1):
        div_b *= index
    return f'{(div_a / div_b):.2f}'


first = int(input())
second = int(input())
print(big_division(first , second))
