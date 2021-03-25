# Write a program, which sums the ASCII codes of n characters and prints the sum on the console.
# Input
# •	On the first line, you will receive n – the number of lines, which will follow
# •	On the next n lines – you will receive letters from the Latin alphabet
# Output
# Print the total sum in the following format:
# The sum equals: {total_sum}
# Constraints
# •	n will be in the interval [1…20].
# •	The characters will always be either upper or lower-case letters from the English alphabet
# •	You will always receive one letter per line
n = int(input())
result = 0
for c in range(1, n + 1):
    character = ord(input())
    result += character
print(f'The sum equals: {result}')
