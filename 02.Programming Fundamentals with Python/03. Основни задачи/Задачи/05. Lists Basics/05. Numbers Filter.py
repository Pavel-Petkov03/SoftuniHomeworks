# You will receive a single number n. On the next n lines you will receive integers.
# After that you will be given one of the following commands:
# •	even
# •	odd
# •	negative
# •	positive
# Filter all the numbers that fit in the category (0 counts as a positive and even). Finally, print the result.
even = []
odd = []
negative = []
positive = []
n = int(input())
for c in range(1, n +1):
    num = int(input())
    if num % 2 == 0 or num == 0:
        even.append(num)
    else:
        odd.append(num)
    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)
command = input()
if command == "even":
    print(even)
elif command == "odd":
    print(odd)
elif command == "positive":
    print(positive)
elif command == "negative":
    print(negative)
