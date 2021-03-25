# You will receive a todo-notes until you get the command "End".
#  The notes will be in the format: "{importance}-{value}". Return the list of
# todo-notes sorted by importance. The maximum importance will be 10
# Hint
# •	Use the insert() method

def importance():
    to_do_list = [0] * 10
    command = input()
    while command != "End":
        actual_command = command.split("-")
        if to_do_list[int(actual_command[0]) - 1] == 0:
            to_do_list.pop(int(actual_command[0]) - 1)
        to_do_list.insert(int(actual_command[0]), actual_command[1])
        command = input()
    result = [element for element in to_do_list if element != 0]
    return result


print(importance())
