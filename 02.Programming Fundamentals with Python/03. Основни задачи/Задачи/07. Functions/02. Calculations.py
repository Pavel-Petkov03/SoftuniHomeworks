# Create a function that receives three parameters and calculates a result depending on operator. The operator can be
# 'multiply', 'divide', 'add', 'subtract' . The input comes as three parameters –
# two integers and an operator as a string.
def calculator(operation, a, b):
    if operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b
    elif operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b


operator = input()
first = int(input())
second = int(input())
print((calculator(operator , first , second)))

