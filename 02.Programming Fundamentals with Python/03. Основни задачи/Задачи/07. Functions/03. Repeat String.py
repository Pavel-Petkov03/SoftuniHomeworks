# Write a function that receives a string and a repeat count n.
# The function should return a new string (the old one repeated n times).
def again(string , times):
    result = ''
    for n in range(1 , times + 1):
        result += string
    return result


needed_string = input()
times_needed = int(input())
print(again(needed_string , times_needed))

