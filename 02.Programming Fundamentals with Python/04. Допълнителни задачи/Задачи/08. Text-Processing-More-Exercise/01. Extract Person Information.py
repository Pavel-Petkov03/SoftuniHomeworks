# Write a program that reads N lines of strings and extracts the name and age of a given person. The name of the person
# will be between '@' and '|'. The person’s age will be between '#' and '*'. Example:
# "Hello my name is @Peter| and I am #20* years old." For each found name and age print a
# line in the following format "{name} is {age} years old."
n = int(input())
for h in range(n):
	comment = input()
	listed = [comment[c] for c in range(len(comment))]
	name = ''.join(listed[listed.index('@')+1:listed.index('|')])
	age = int(''.join(listed[listed.index('#')+1:listed.index('*')]))
	print(f"{name} is {age} years old.")







