# First you will be given a sequence of integers representing males.
# Afterwards you will be given another sequence of integers representing females.
# You have to start from the first female and try to match it with the last male.
# •	If their values are equal, you have to match them and remove both of
# them. Otherwise you should remove only the female and decrease the value of the male by 2.
# •	If someone’s value is equal to or below 0, you should remove him/her
# from the records before trying to match him/her with anybody.
# •	Special case - if someone’s value divisible by 25 without remainder,
# you should remove him/her and the next person of the same gender.
# You need to stop matching people when you have no more females or males.
# Input
# •	On the first line of input you will receive the integers, representing the males, separated by a single space.
# •	On the second line of input you will receive the integers, representing the females, separated by a single space.
# Output
# •	On the first line of output - print the number of successful matches:
# o	"Matches: {matchesCount}"
# •	On the second line - print all males left:
# o	If there are no males: "Males left: none"
# o	If there are males: "Males left: {maleN}, … , {male3}, {male2}, {male1}"
# •	On the third line - print all females left:
# o	If there are no females: "Females left: none"
# o	If there are females: "Females left: {female1}, {female2}, {female3},…, {femaleN}"
# Constraints
# •	All of the given numbers will be valid integers in the range [-100, 100].
from collections import deque

males = list(map(int, input().split()))
females = deque(list(map(int, input().split())))
matches = 0
while females and males:
    current_male = males[-1]
    current_female = females[0]
    if (current_male % 25 == 0 or current_female % 25 == 0) and (0 not in (current_female, current_male)):
        if current_male % 25 == 0:
            males.pop()
            males.pop()
        else:
            females.popleft()
            females.popleft()
    elif current_female <= 0 or current_male <= 0:
        if current_female <= 0:
            females.popleft()
        else:
            males.pop()

    else:
        if current_male == current_female:
            females.popleft()
            males.pop()
            matches += 1
        else:
            females.popleft()
            males[-1] -= 2

print(f"Matches: {matches}")
if males:
    res_m = f"Males left: {', '.join(list(map(str, reversed(males))))}"
else:
    res_m = "Males left: none"
if females:
    res_f = f"Females left: {', '.join(list(map(str, females)))}"
else:
    res_f = "Females left: none"

print(res_m)
print(res_f)

