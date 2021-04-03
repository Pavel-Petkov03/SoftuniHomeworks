my_word = input()
command = input()
while command != 'End':
    command = command.split()
    if command[0] == 'Translate':
        _, char, replacement = command
        my_word = my_word.replace(char, replacement)
        print(my_word)
    elif command[0] == 'Includes':
        _, string = command
        if string in my_word:
            print("True")
        else:
            print("False")
    elif command[0] == 'Start':
        _, string = command
        length = len(string)
        if my_word[:length] == string:
            print('True')
        else:
            print('False')
    elif command[0] == 'Lowercase':
        my_word = my_word.lower()
        print(my_word)
    elif command[0] == 'FindIndex':
        _, char = command
        wanted_index = None
        for last_index in range(len(my_word) - 1, -1, -1):
            if my_word[last_index] == char:
                wanted_index = last_index
                break
        print(wanted_index)
    elif command[0] == 'Remove':
        _, start, count = command
        start, count = int(start), int(count)
        my_word = my_word[:start] + my_word[start+count:]
        print(my_word)
    command = input()
