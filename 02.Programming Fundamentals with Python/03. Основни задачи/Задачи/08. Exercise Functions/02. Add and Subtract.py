# You will receive three integer numbers.
# Write a function sum_numbers() to get the sum of the first two integers and subtract()
# function that subtracts the third integer from the result. Wrap the two functions in
# a function called add_and_subtract() which will receive the three numbers

def add_and_subtract(a , b , c):
    def sum_numbers():
        result = a + b
        return result
    def subtract():
        final_result = sum_numbers() - c
        return final_result
    return subtract()


first = int(input())
second = int(input())
third = int(input())

print(add_and_subtract(first , second , third))
