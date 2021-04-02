# The SoftUni Spelling Bee competition is here. But it`s not like any other Spelling Bee competition out there,
# it`s different and a lot more fun! You, of course, are a participant and you are eager to show the competition
# that you are the best, so go ahead, learn the rules and win!
# On the first line of the input you will be given a text string. In order to win the competition you have to
# find all hidden word pairs, read them and mark the ones that are mirror images of each other.
# First of all you have to extract the hidden word pairs. Hidden word pairs are:
# •	Surrounded by "@" or "#" (only one of the two) in the following pattern #wordOne##wordTwo# or @wordOne@@wordTwo@
# •	At least 3 characters long each (without the surrounding symbols)
# •	Made up of letters only
# If the second word, spelled backwards is the same as the first word and vice versa (casing matters!),
# then they are a match and you have to store them somewhere. Examples of mirror words:
# #Part##traP# @leveL@@Level@ #sAw##wAs#
# •	If you don`t find any valid pairs print: "No word pairs found!"
# •	If you find valid pairs print their count: "{valid pairs count} word pairs found!"
# •	If there are no mirror words print: "No mirror words!"
# •	If there are mirror words print:
# "The mirror words are:
# {wordOne} <=> {wordtwo}, {wordOne} <=> {wordtwo}, {wordOne} <=> {wordtwo}, etc…"
# Input / Constraints
# •	You will recive a string.
# Output
# •	Print the proper output messages in the proper cases as described in the problem description.
# •	If there are pairs of mirror words, print them in the end, each pair separated by ", ".
# •	Each pair of mirror word must be printed with " <=> " between the words.
import re
text = input()
valid = []
mirror = []
pattern = r'([@#])(?P<first>([A-Za-z]{2,}+))\1\1(?P<second>([A-Za-z]{2,}+))\1'
for c in re.finditer(pattern, text):
	p = c.groupdict()
	valid.append(p)
	if p['first'] == p['second'][::-1]:
		mirror.append(f"{p['first']} <=> {p['second']}")

if len(valid) != 0:
	print(f'{len(valid)} word pairs found!')
else:
	print("No word pairs found!")
if len(mirror) != 0:
	print('The mirror words are:')
	print(', '.join(mirror))
else:
	print("No mirror words!")