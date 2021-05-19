n = int(input())
divide = int(input())
score = 0
if n % 2 != 0:
    score += 1
if n < 0:
    score += 1
if n % divide == 0:
    score += 1

if score == 0:
    print('boring')
elif score == 1:
    print('awesome')
elif score == 2:
    print('super awesome')
elif score == 3:
    print('super special awesome')
