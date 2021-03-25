# Write a program to read an integer n and print all triples of the first n small Latin letters,
# ordered alphabetically:
n = int(input())
for first in range(0 , n):
    for second in range( 0, n ):
        for third in range( 0, n ):
            print(f'{chr(97 + first)}{chr(97 + second)}{chr(97 + third)}')
