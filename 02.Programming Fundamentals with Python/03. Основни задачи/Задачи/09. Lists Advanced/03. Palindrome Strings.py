# Write a program that receives on the first line words separated
# by a space and a searched palindrome on the second.
# Print all the palindromes on the first line.
# Print all the occurrences of the searched palindrome in the format:
# "Found palindrome {count} times"
def palindrome(big_string , count_word):
    splited_string = big_string.split()
    palindrom_list = [splited_string[pal] for pal in range(len(splited_string)) if splited_string[pal] == splited_string[pal][::-1]]
    print(palindrom_list)
    return f"Found palindrome {big_string.count(count_word)} times"
our_str = input()
word = input()
print(palindrome(our_str , word))
