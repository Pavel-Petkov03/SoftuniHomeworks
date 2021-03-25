# In the "Tribonacci" sequence, every number is formed by the sum of the previous 3.
# You are given a number num. Write a program that prints num numbers from the Tribonacci sequence, each on a new line, starting from 1. The input comes as a parameter named num. The value num will always be positive integer.
def tribonachi(times):
    result = ''
    first = 0
    second = 0
    third = 0
    for times in range( 1, num + 1 ):
        if times == 1:
            first = 1
            result += f"{first} "
        elif times == 2:
            second = first
            result += f"{second} "
        elif times == 3:
            third = 2
            result += f"{third} "
        else:
            actual_first = first
            actual_second = second
            actual_third = third
            first = actual_second
            second = actual_third
            third = actual_second + actual_third + actual_first
            result += f"{third} "

    return result
num = int(input())
print(tribonachi(num))

