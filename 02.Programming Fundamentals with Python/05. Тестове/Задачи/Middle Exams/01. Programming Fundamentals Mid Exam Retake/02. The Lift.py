# Write a program that finds a place for the tourist on a lift.
# Every wagon should have a maximum of 4 people on it. If a wagon is full you
# should direct the people to the next one with space available.
# Input
# 	On the first line you, will receive how many people are waiting to get on the lift
# 	On the second line, you will you will receive the current state of the lift separated by " ".
# Output
# When there is no more available space left on the lift, or there are no more people in the
# queue, you should print on the console the final state of the lift's wagons separated by " "
# and one of the following messages:
# 	If there are no more people and the lift have empty spots you should print:
# "The lift has empty spots!
# {wagons separated by ' '}"
# 	If there are still people on the queue and no more available space, you should print:
# "There isn't enough space! {people} people in a queue!
# {wagons separated by ' '}"
# 	If the lift is full and there are no more people in the queue, you should print only the wagons separated by " "

people = int(input())
wagons = input().split()
wagons_list = [int(wagons[c])for c in range(len(wagons))]
for fill in range(len(wagons_list)):
	if people < 4:
		wagons_list[fill] += people
		people = 0
		break
	else:
		people -= 4 - wagons_list[fill]
		wagons_list[fill] += 4 - wagons_list[fill]

for_list = [c for c in wagons_list if c == 4]
wagons_list = [str(el) for el in wagons_list]
if len(for_list) != len(wagons_list):
	print("The lift has empty spots!")
	print(" ".join(wagons_list))
elif people > 0 and len(for_list) == len(wagons_list):
	print(f"There isn't enough space! {people} people in a queue!")
	print(" ".join(wagons_list))
else:
	print(" ".join(wagons_list))

