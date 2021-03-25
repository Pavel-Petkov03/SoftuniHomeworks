# Using a comprehension write a program that receives a text and removes all the vowels from it, case
# insensitive. Print the new text string after removing the vowels. The vowels that should be considered are
# 'a', 'o', 'u', 'e', 'i'.
vowels = 'aouei'
print(''.join([c for c in list(input()) if c not in vowels]))