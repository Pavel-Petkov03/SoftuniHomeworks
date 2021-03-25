# You are given a number num1, num2 and num3. Write a program that finds if num1 * num2 * num3 (the product) is negative, positive or zero. Try to do this WITHOUT multiplying the 3 numbers.
def multiply(first , second , third):
    negativity = 0
    if float(first) < 0:
        negativity += 1
    elif float(first) == 0:
        return 'zero'
    if float(second) < 0:
        negativity += 1
    elif float(second) == 0:
        return 'zero'
    if float(third) < 0:
        negativity += 1
    elif float(third) == 0:
        return 'zero'
    if negativity % 2 == 0 or negativity == 0:
        return "positive"
    else:
        return "negative"

our_first = input()
our_second = input()
our_third = input()
print(multiply(our_first , our_second , our_third))

