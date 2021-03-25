# Габи иска да започне здравословен начин на живот и си е поставила за цел да върви 10 000
# стъпки всеки ден. Някои дни обаче е много уморена от работа и ще иска да се прибере преди
# да постигне целта си. Напишете програма, която чете от конзолата по колко стъпки изминава
# тя всеки път като излиза през деня и когато постигне целта си да се изписва
# "Goal reached! Good job!" и колко стъпки повече е извървяла "{разликата между стъпките}
# steps over the goal!"
# Ако иска да се прибере преди това, тя ще въведе командата "Going home" и ще въведе стъпките,
# които е извървяла докато се прибира. След което, ако не е успяла да постигне целта си,
# на конзолата трябва да се изпише: "{разликата между стъпките} more steps to reach goal."
wanted_steps = 10000
steps = input()
all_steps = 0
goal_reach = False
last_steps = 0
while steps != "Going home":
    steps = int(steps)
    all_steps += steps
    if wanted_steps <= all_steps:
        goal_reach = True
        break
    steps = input()
if steps == "Going home":
    last_steps = int(input())
    all_steps += last_steps
    if wanted_steps <= all_steps:
        goal_reach = True

diff = abs(wanted_steps - all_steps)
if goal_reach:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")




















