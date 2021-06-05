# Write a program that receives names on the first line (separated by comma and space ", ") and number of chairs
# on the second line (an integer). Find all the ways to fit those people on the
# chairs. Print each combination on a separate line.

perm_list = list(input())


def permute(my_list, current_index=0):
    if current_index == len(my_list):
        print(my_list)
        return
    for i in range(current_index, len(my_list)):
        my_list[current_index], my_list[i] = my_list[i], my_list[current_index]
        permute(my_list, current_index + 1)
        my_list[current_index], my_list[i] = my_list[i], my_list[current_index]


permute(perm_list)