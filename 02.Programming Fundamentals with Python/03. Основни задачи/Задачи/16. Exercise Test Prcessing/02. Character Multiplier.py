# Create a program that receives two strings on a single lines separated by space and prints the sum of their character
# codes multiplied (multiply str1[0] with str2[0] and add to the total sum). Then continue with the next two characters.
# If one of the strings is longer than the other, add the remaining character codes to the total sum without
# multiplication.


strings = input().split()
if len(strings[0]) >= len(strings[1]):
	length = len(strings[1])
	greater = len(strings[0]) - len(strings[1])
	place = strings[0]
else:
	length = len(strings[0])
	greater = len(strings[1]) - len(strings[0])
	place = strings[1]

sum_ = 0
for index in range(length):
	sum_ += ord(strings[0][index]) * ord(strings[1][index])

for index in range(greater):
	sum_ += ord(place[len(place) - 1 - index])

print(sum_)