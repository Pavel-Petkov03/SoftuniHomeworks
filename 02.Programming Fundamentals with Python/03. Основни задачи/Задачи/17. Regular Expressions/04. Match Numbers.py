# Write a program, which finds all integer and floating-point numbers in a string.
# Compose the Regular Expression
# A number has the following characteristics:
# •	Has either whitespace before it or the start of the string (match either ^ or what's called a positive
# lookbehind). The entire syntax for the beginning of your RegEx might look something like "(^|(?<=\s))".
# •	The number might or might not be negative, so it might have a hyphen on its left side ("-").
# •	Consists of one or more digits.
# •	Might or might not have digits after the decimal point
# •	The decimal part (if it exists) consists of a period (".") and one or more digits after it.
# 	Use a capturing group.
# •	Has either whitespace before it or the end of the string
# (match either $ or what's called a positive lookahead). The syntax for the end of the
# RegEx might look something like "($|(?=\s))".
# Let's see how we would translate the above rules into a regular expression:
# •	First off, we need to establish what needs to exist before our number.
# 	We can't use \b here, since it includes "-", which we need to match negative numbers.
# Instead, we'll use a positive lookbehind, which matches if there's
# something immediately behind it. We'll match if we're either at the start of the string (^), or if
# there's any whitespace behind the string:
import re
pattern = r'(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))'
nums = re.finditer(pattern, input())
print(*[c.group() for c in nums])
