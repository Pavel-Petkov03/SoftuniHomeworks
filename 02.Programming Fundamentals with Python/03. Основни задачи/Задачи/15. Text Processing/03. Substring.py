# On the first line you will receive a string. On the second line you will receive a second string. Write a program that
# removes all of the occurrences of the first string in the second until there is no match. At the end print the
# remaining string.

outing_str = input()
removal_string = input()
while outing_str in removal_string:
	removal_string = removal_string.replace(outing_str, '')

print(removal_string)
