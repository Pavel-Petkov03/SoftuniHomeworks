# Find online more information about ASCII (American Standard Code for Information Interchange)
# and write a program that prints part of the ASCII table of characters on the
# console.  On the first line of input you will receive
# the char index you should start with and on the second line - the index of the last character you should print.
start = int(input())
finish = int(input())
result = ''
for c in range(start, finish + 1):
    symbol = chr(c)
    result += symbol + ' '
print(result)