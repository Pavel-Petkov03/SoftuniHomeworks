# So you've found a meeting room - phew! You arrive there ready to present, and find that someone
# has taken one or more of the chairs!! You need to find some quick.... check all the other meeting
# rooms to see if all of the chairs are in use.
# You will be given a number n representing how many rooms there are. On the next n lines for each room
# you will get how many chairs there are and how many of them will be taken. The chairs will be represented
# by "X"s, then there will be a space " " and a number representing the taken places. Example: "XXXXX 4"
# (5 chairs and 1 of them is left free). Keep track of the free chairs, you will need them later. However i
# f you get to a room where there are more people than chairs, print the following message: "{needed_chairs_in_room}
# more chairs needed in room {number_of_room}". If there is enough chairs in each room print: "Game On,
# {total_free_chairs} free chairs left"

free_chairs = 0
is_good = True
n = int(input())
for times in range(1 , n + 1):
	array = input()
	chairs, taken = array.split()
	taken = int(taken)
	if len(chairs) < taken:
		print(f'{taken - len(chairs)} more chairs needed in room {times}')
		is_good = False
	else:
		free_chairs += len(chairs) - taken
if is_good:
	print(f'Game On, {free_chairs} free chairs left')











