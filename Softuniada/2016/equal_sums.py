from itertools import permutations

first = int(input())
second = int(input())
third = int(input())
forth = int(input())
is_found = False
new = list(permutations([first, second, third, forth]))
for tup in new:
    first, second, third, forth = tup
    if first + second == third + forth:
        print('Yes')
        print(first + second)
        is_found = True
        break
    elif first == second + third + forth:
        print('Yes')
        print(first)
        is_found = True
        break

if not is_found:
    print('No')
