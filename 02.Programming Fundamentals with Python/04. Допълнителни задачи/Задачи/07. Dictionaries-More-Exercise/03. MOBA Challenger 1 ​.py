# Pesho is a pro MOBA player, he is struggling to become а master of the Challenger tier. So
# he watches carefully the statistics in the tier.
# You will receive several input lines in one of the following formats:
# "{player} -> {position} -> {skill}"
# "{player} vs {player}"
# The player and position are strings, the given skill will be an integer number.
# You need to keep track of every player.
# When you receive a player and his position and skill, add him to the player pool,
# if he isn`t present, else add his position and skill or update his skill, only if the
# current position skill is lower than the new value.
# If you receive "{player} vs {player}" and both players exist in the tier, they duel with the following rules:
# Compare their positions, if they got at least one in common, the player with better
# total skill points wins and the other is demoted from the tier -> remove him.
# If they have same total skill points, the duel is tie and they both continue in the Season.
# If they don`t have positions in common, the duel isn`t happening and both continue in the Season.
# You should end your program when you receive the command "Season end".
# At that point you should print the players, ordered by total skill in desecending order,
# then ordered by player name in ascending order. Foreach player print their position and skill,
# ordered desecending by skill, then ordered by position name in ascending order.
# Input / Constraints
# •	The input comes in the form of commands in one of the formats specified above.
# •	Player and position will always be one word string, containing no whitespaces.
# •	Skill will be an integer in the range [0, 1000].
# •	There will be no invalid input lines.
# •	The programm ends when you receive the command "Season end".
# Output
# •	The output format for each player is:
# "{player}: {totalSkill} skill"
# "- {position} <::> {skill}"

def add_(dict_, player_, position_, skill_):
	if player_ in dict_:
		if position_ in dict_[player_]:
			if int(dict_[player_][position_]) < int(skill_):
				dict_[player_][position_] = int(skill_)
		else:
			dict_[player_].update({position_: int(skill_)})
	else:
		dict_[player_] = {position_: int(skill_)}

	return dict_


def duel(dict_, player_1_, player_2_):
	if player_1_ in dict_ and player_2_ in dict_:
		for place, p in dict_[player_1_].items():
			if place in dict_[player_2_]:
				first_p = sum(dict_[player_1_].values())
				second_p = sum(dict_[player_2_].values())
				if first_p > second_p:
					dict_.pop(player_2_)
				elif second_p > first_p:
					dict_.pop(player_1_)
				return dict_

	return dict_



duel_dict = {}
command = input()
while command != "Season end":
	if " -> " in command:
		player, position, skill = command.split(" -> ")
		duel_dict = add_(duel_dict, player, position , skill)
	else:
		player_1, player_2 = command.split(" vs ")
		our_dict = duel(duel_dict, player_1, player_2)

	command = input()

for name, place_and_p in sorted(duel_dict.items(), key=lambda b: (-sum(b[1].values()), b[0])):
	print(f'{name}: {sum(place_and_p.values())} skill')
	for place, p in sorted(place_and_p.items(), key=lambda n: (-int(n[1]), n[0])):
		print(f'- {place} <::> {p}')

