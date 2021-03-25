# A palindrome is a number which reads the same backward as forward, such as 323 or 1001.
# Write a function which receives
# a list of positive integers and checks if each integer is a palindrome or not. Print the results on the console
# The input will be a single string containing the numbers separated by comma and space ", "
def palindrome(text):
    our_list = text.split(", ")
    match1 = ""
    match2 = ''
    actual_result = ""
    for index in range(len(our_list)):
        for forward in range(len(our_list[index])):
            match1 += f"{our_list[index][forward]}"
        for backward in reversed(range(len(our_list[index]))):
            match2 += f"{our_list[index][backward]}"
        if match1 == match2:
            actual_result += "True\n"
        else:
            actual_result += "False\n"
        match1 = ''
        match2 = ''
    return actual_result


our_text = input()
print(palindrome(our_text))


