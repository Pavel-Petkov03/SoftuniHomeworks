# for every unique forceUser, registered in the application.
# You will receive several input lines in one of the following formats:
# {forceSide} | {forceUser}
# {forceUser} -> {forceSide}
# The forceUser and forceSide are strings, containing any character.
# If you receive forceSide | forceUser, you should check if such forceUser already exists,
# and if not, add him/her to the corresponding side.
# If you receive a forceUser -> forceSide, you should check if there is such a forceUser
# already and if so, change his/her side. If there is no such forceUser, add him/her to the
# corresponding forceSide, treating the command as a new registered forceUser.
# Then you should print on the console: "{forceUser} joins the {forceSide} side!"
# You should end your program when you receive the command "Lumpawaroo". At that point you
# should print each force side, ordered descending by forceUsers count, than ordered by name.
# For each side print the forceUsers, ordered by name.
# In case there are no forceUsers in a side, you shouldn`t print the side information.
# Input / Constraints
# •	The input comes in the form of commands in one of the formats specified above.
# •	The input ends, when you receive the command "Lumpawaroo".
# Output
# •	As output for each forceSide, ordered descending by forceUsers count, then by name,
# you must print all the forceUsers, ordered by name alphabetically.
# •	The output format is:
# Side: {forceSide}, Members: {forceUsers.Count}
# ! {forceUser}
# ! {forceUser}
# ! {forceUser}
# •	In case there are NO forceUsers, don`t print this side.
def add(dict_, our_side , our_user):
	for side , users in our_dict.items():
		if our_user in users:
			return dict_
	if our_side not in dict_:
		dict_[our_side] = []
		dict_[our_side].append(our_user)
	else:
		if our_user not in dict_[our_side]:
			dict_[our_side].append(our_user)
	return dict_

def convert(dict_ , our_user , our_side):
	for side, users in dict_.items():
		if our_user in users:
			dict_[side].remove(our_user)
			return add(dict_,our_side,our_user)
	return add(dict_, our_side, our_user)


our_dict = {}
command = input()
while command != "Lumpawaroo":
	if " | " in command:
		side , user = command.split(" | ")
		dict_ = add(our_dict ,side , user )
	elif " -> " in command:
		user, side = command.split(" -> ")
		dict_ = convert(our_dict , user , side)
		print( f'{user} joins the {side} side!' )
	command = input()

for key, value in sorted(our_dict.items(), key= lambda x: (-len(x[1]), x[0])):
	if len(value) != 0:
		print(f'Side: {key}, Members: {len(value)}')
		for string in sorted(value):
			print(f'! {string}')

# e | b
# e | a
# f | c
# f | d
# f | e
# g | e
# Lumpawaroo

