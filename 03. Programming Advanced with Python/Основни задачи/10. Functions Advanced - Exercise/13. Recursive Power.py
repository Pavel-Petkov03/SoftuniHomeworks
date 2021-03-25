# Create a recursive function called recursive_power which should receive a number and a power.
# Using recursion return the result of number ** power. Submit only the function in the judge system.


def recursive_power(num, power):
    if power == 1:
        return num
    return num * recursive_power(num, power - 1)


print(recursive_power(12, 2))
