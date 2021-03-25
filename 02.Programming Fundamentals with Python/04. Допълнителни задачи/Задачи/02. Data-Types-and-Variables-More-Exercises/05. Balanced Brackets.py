# You will receive n lines. On those lines, you will receive one of the following:
# •	Opening bracket – “(“,
# •	Closing bracket – “)” or
# •	Random string
# Your task is to find out if the brackets are balanced.
# That means after every closing bracket should follow an opening one.
# Nested parentheses are not valid,
# and if two consecutive opening brackets exist, the expression should be marked as unbalanced.
# Input
# •	On the first line, you will receive n – the number of lines, which will follow
# •	On the next n lines, you will receive “(”, “)” or another string
# Output
# You have to print “BALANCED”, if the parentheses are balanced and “UNBALANCED” otherwise.
n = int(input())
times1 = 0
times2 = 0
is_open = False
is_break = False
for c in range(1, n + 1):
    symbol = input()
    if symbol == "(":
        is_open = True
        times1 += 1
        times2 = 0
        if times1 == 2:
            is_break = True
            break
    elif symbol == ")":
        times2 += 1
        if times2 == 2:
            is_break = True
            break
        if is_open:
            is_open = False
            times1 = 0
if is_break:
    print("UNBALANCED")
else:
    print("BALANCED")








