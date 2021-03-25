# Write a program that prints a sum of all characters between two given characters (their ascii code). On the first
# line you will get a character. On the second line you get another character. On the last line you get a random
# string. Find all the characters between the two given and print their ascii sum.
start = input()
end = input()
string = input()
sum_ = 0
for char in string:
	if ord(start) + 1 <= ord(char) <= ord(end) - 1:
		sum_ += ord(char)

print(sum_)