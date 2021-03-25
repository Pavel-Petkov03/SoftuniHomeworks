# You will receive a command and a list of numbers:
# If the command is "Odd": Print the sum of the Odd numbers multiplied by the length of the initial list.
# If the command is "Even": Print the sum of the Even numbers multiplied by the length of the initial list



key = input()
initial_list = list(map(int, input().split()))


def odd(m_list):
    return sum([c for c in m_list if c % 2 != 0]) * len(m_list)


def even(m_list):
    return sum([c for c in m_list if c % 2 == 0]) * len(m_list)


doing_dict = {'Odd': odd(initial_list), 'Even': even(initial_list)}
print(doing_dict[key])
