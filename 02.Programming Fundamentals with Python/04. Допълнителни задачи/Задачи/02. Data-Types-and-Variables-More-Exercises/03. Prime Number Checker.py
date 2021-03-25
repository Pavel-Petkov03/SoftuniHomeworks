# Write a program to check if a number is prime (only wholly divisible by itself and one).
# The input comes as an integer number.
# The output should be true for prime number and false otherwise.
number = int(input())
is_prime = None
for match in range(2 , number):
    if number % match == 0:
        is_prime = False
        break
    else:
        is_prime = True

if is_prime:
    print("True")
else:
    print("False")
    