# Using a list comprehension, write a program that receives some text, separated by comma and space ", ",
# and prints on the console each string with its length in the following format:
# "{first_str} -> {first_str_len}, {second_str} -> {second_str_len},…"


my_list = input().split(', ')
print(', '.join([f'{c} -> {len(c)}'for c in my_list]))