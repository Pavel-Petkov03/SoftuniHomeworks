# Write a program that finds, how many times a given word, is used in a given sentence.
# Note that letter case does not matter – it is case-insensitive.
# The output is a single number indicating the amount of times the sentence contains the word.

import re
text = input()
pattern = f"\\b{input()}\\b"
a = 5
print(len(re.findall(pattern, text,flags=re.IGNORECASE)))

