# Tony and Andi love playing in the snow and having snowball fights,
# but they always argue which makes the best snowballs.
# They have decided to involve you in their fray,
# by making you write a program, which calculates snowball data, and outputs the best snowball value.
# You will receive N – an integer, the number of snowballs being made by Tony and Andi.
# For each snowball you will receive 3 input lines:
# •	On the first line you will get the snowball_snow – an integer.
# •	On the second line you will get the snowball_time – an integer.
# •	On the third line you will get the snowball_quality – an integer.
# For each snowball you must calculate its snowball_value by the following formula:
# (snowball_snow / snowball_time) ^ snowball_quality
# At the end you must print the highest calculated snowball_value.
# Input
# •	On the first input line you will receive N – the number of snowballs.
# •	On the next N * 3 input lines you will be receiving data about snowballs.
# Output
# •	As output you must print the highest calculated snowball_value, by the formula, specified above.
# •	The output format is:
# {snowball_snow} : {snowball_time} = {snowball_value} ({snowball_quality})
# Constraints
# •	The number of snowballs (N) will be an integer in range [0, 100].
# •	The snowball_snow is an integer in range [0, 1000].
# •	The snowball_time is an integer in range [1, 500].
# •	The snowball_quality is an integer in range [0, 100].
import sys
n = int(input())
max = -sys.maxsize
snowball_snow = None
snowball_time = None
snowball_quality = None
snowball_value = None
initial_snowball_snow =None
initial_snowball_time = None
initial_snowball_quality = None
for ball in range(1, n + 1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = int(snowball_snow / snowball_time) ** snowball_quality
    if snowball_value > max:
        max = snowball_value
        initial_snowball_snow = snowball_snow
        initial_snowball_time = snowball_time
        initial_snowball_quality = snowball_quality
print(f'{initial_snowball_snow} : {initial_snowball_time} = {max} ({initial_snowball_quality})')


