# Write a program, which matches a date in the format "dd{separator}MMM{separator}yyyy".
# Use capturing groups in your regular expression.
# Compose the Regular Expression
# Every valid date has the following characteristics:
# •	Always starts with two digits, followed by a separator
# •	After that, it has one uppercase and two lowercase letters (e.g. Jan, Mar).
# •	After that, it has a separator and exactly 4 digits (for the year).
# •	The separator could be either of three things: a period ("."), a hyphen ("-") or a forward slash ("/")
# •	The separator needs to be the same for the whole date (e.g. 13.03.2016 is valid,
# 13.03/2016 is NOT). Use a group backreference to check for this.
# You can follow the table below to help with composing your RegEx:
import re
pattern = r'\b(?P<date>[0-9]{2})(?P<separator>[./-])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>[0-9]{4})\b'
our_date = input()
filtered = re.finditer(pattern, our_date)
for date in filtered:
	d = date.groupdict()
	print(f'Day: {d["date"]}, Month: {d["month"]}, Year: {d["year"]}')




