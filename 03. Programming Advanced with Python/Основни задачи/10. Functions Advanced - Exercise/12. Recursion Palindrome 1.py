# Write a recursive function called palindrome which will receive a word and an index (always 0).
# Implement the function, so it returns "{word} is a palindrome" if the word is a palindrome and
# "{word} is not a palindrome" if the word is not a palindrome using recursion. Submit only the
# function in the judge system.


def palindrome(my_str, index=0, right_index=-1):
    if index == len(my_str) // 2:
        return f"{my_str} is a palindrome"
    if my_str[index] == my_str[right_index]:
        return palindrome(my_str, index + 1, right_index - 1)
    else:
        return f'{my_str} is not a palindrome'


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
