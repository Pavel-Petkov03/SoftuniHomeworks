# //You will receive a single integer number between 0 and 100 which is divided with 10 without residue
# (0, 10, 20, 30...).
# Your task is to create a function that visualizes a
# loading bar depending on that number you have received in the input.

# def bar_fill(percent):
#     final = ''
#     is_hundred = None
#     final_result = ''
#     for fill in range(0 , percent , 10):
#         final += "%"
#         is_hundred = True
#     for fill in range(percent ,100 , 10):
#         is_hundred = False
#         final += "."
#
#     if is_hundred:
#         final_result += "100% Complete!\n"
#         final_result += '[%%%%%%%%%%]'
#     else:
#         final_result += f'{percent}% [{final}]\n'
#         final_result += 'Still loading...'
#
#     return final_result
#
#
# our_percent = int(input())
# print(bar_fill(our_percent))

completeness_bar = []
def completness_check(percentage , com):
    completness_range = int(percentage / 10)

    for i in range( completness_range ):
        com.append('%')
    for j in range(len(com), 10):
        com.append('.')
    com = ''.join(com)

    if percentage == 100:
        result_text = "100% Complete!"
    else:
        result_text = "Still loading..."

    return (com, result_text)


number = int(input())
if number != 100:
    print(f"{number}% [{completness_check(number , completeness_bar)[0]}]" )
    print(completness_check(number, completeness_bar)[1])
else:
    print('100% Complete!')
    print('[%%%%%%%%%%]')

