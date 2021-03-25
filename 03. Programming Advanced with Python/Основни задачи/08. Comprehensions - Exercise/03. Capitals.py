# Using a dictionary comprehension, write a program that receives country
# names on the first line, separated by comma and space ", ", and their corresponding capital cities on the second
# line (again separated by comma and space ", ") and prints each country, with their capital, on a separate
# line in the following format:
# "{country} -> {capital}"
# Hints
# •	You can use the zip() method to zip the two lists into tuple pairs.


county = input().split(', ')
town = input().split(', ')
mix = list((zip(county, town)))
[print(f'{c[0]} -> {c[1]}') for c in mix]