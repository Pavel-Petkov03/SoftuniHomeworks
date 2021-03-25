# Write a function that receives an integer number and returns if this number is perfect or NOT.
# A perfect number is a positive integer that is equal to the sum of its proper positive divisors. That is the sum of
# its positive divisors excluding the number itself (also known as its aliquot sum).
def perfect(num):
    sum_all = 0
    for divider in range(1 , num):
        if num % divider == 0:
            sum_all += divider
    if sum_all == num:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


actual_num = int(input())
print(perfect(actual_num))
