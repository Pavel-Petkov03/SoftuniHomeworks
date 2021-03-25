# Write a program that generates all the possible expressions and their results between a given list
# of numbers using only the + and - operators. Print them on the console as shown in the example

nums = list(map(int, input().split(", ")))


def expressions(my_list, my_sum=0, exp=''):
    if not my_list:
        return [(exp, my_sum)]

    plus = expressions(my_list[1:], my_sum + my_list[0], exp + f'+{my_list[0]}')
    minus = expressions(my_list[1:], my_sum - my_list[0], exp + f'-{my_list[0]}')
    return plus + minus


[print(f'{c[0]}={c[1]}') for c in expressions(nums)]
