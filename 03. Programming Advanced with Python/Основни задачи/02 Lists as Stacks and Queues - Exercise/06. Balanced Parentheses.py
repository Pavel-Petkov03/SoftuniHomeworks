# Given a sequence consisting of parentheses, determine whether the expression
# is balanced. A sequence of parentheses is balanced if every open parenthesis can be
# paired uniquely with a closed parenthesis that occurs after the former. Also, the interval
# between them must be balanced. You will be given three types of parentheses: (, {, and [.
# {[()]} - This is a balanced parenthesis.
# {[(])} - This is not a balanced parenthesis.
# Input
# •	Each input consists of a single line, the sequence of parentheses.
# Output
# •	For each test case, print on a new line "YES" if the parentheses are balanced.
# Otherwise, print "NO". Do not print the quotes.

stack = []
is_no = False
for c in input():
    if c == '{' or c == '[' or c == '(':
        stack.append(c)
    else:
        if stack:
            if c == '}':
                if stack.pop() != '{':
                    print('NO')
                    is_no = True
                    break
            elif c == ']':
                if stack.pop() != '[':
                    print('NO')
                    is_no = True
                    break
            else:
                if stack.pop() != '(':
                    print('NO')
                    is_no = True
                    break
        else:
            print('NO')
            is_no = True
            break

if not is_no:
    print('YES')