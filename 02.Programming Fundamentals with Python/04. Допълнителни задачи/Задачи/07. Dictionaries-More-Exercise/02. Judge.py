# You know the jude system, right?! Your job is to create a program similar to the Judge system.
# You will receive several input lines in one of the following formats:
# {username} -> {contest} -> {points}
# The contestName and username are strings, the given points will be an integer number.
# You need to keep track of every contest and individual statistics of every user.
# You should check if such contest already exists, and if not, add it, otherwise check
# if the current user Is participating in the contest, if he is participating take the
# higher score, otherwise just add it.
# Also you need to keep individual statistics for each user - the total points of all contests.
# You should end your program when you receive the command "no more time". At that point you should print each
# contest in order of input, for each contest print the participants ordered by points in descending order,
# than ordered by name in ascending order.  After that, you should print individual statistics for every
# participant ordered by total points in descending order, and then by alphabetical order.
# Input / Constraints
# •	The input comes in the form of commands in one of the formats specified above.
# •	Username and contest name always will be one word.
# •	Points will be an integer will be an integer in range [0, 1000].
# •	There will be no invalid input lines.
# •	If all sorting criteria fail, the order should be by order of input.
# •	The input ends when you receive the command "no more time".
# Output
# •	The output format for the contests is:
# {contestName}: {participants.Count} participants
# {position}. {username} <::> {points}
# •	After you print all contests, print the individual statistics for every participant.
# •	The output format is:
# Individual standings:
# {position}. {username} -> {totalPoints}




def add_(dict_, name_, contest_, points_):
	if contest_ in dict_:
		if name_ in dict_[contest_]:
			if int(dict_[contest_][name_]) < int(points_):
				dict_[contest_][name_] = points_
		else:
			dict_[contest_].update({name_: points_})
	else:
		dict_[contest_] = {name_: points_}

	return dict_


def best_score(dict_):
	new_dict = {}
	for cont, user_and_p in dict_.items():
		for user, p in user_and_p.items():
			if user in new_dict:
				new_dict[user] += int(p)
			else:
				new_dict[user] = int(p)
	return new_dict



our_dict = {}
command = input()
while command != "no more time":
	name, contest, points = command.split(" -> ")
	our_dict = add_(our_dict,name, contest, points)

	command = input()
best_result = best_score(our_dict)
for contest, name_and_points in our_dict.items():
	print(f'{contest}: {len(name_and_points)} participants')
	position = 1
	for name, points in sorted(name_and_points.items(), key=lambda y: (-int(y[1]), y[0])):
		print(f'{position}. {name} <::> {points}')
		position += 1

position = 1
print('Individual standings:')
for name , result in sorted(best_result.items(), key=lambda z: (-int(z[1]), z[0])):
	print(f'{position}. {name} -> {result}')
	position += 1