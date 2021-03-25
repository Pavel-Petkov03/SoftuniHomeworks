# SoftUni just got a new parking lot. It's so fancy, it even has online parking validation. Except the online service ' \
#                                       'doesn't work. It can only receive users' data, but it doesn't know what to do
# with it. Good thing you're on the dev team and know how to fix it, right?
# Write a program, which validates a parking place for an online service. Users can register to park and unregister to leave.
# The program receives 2 types of commands:
# 	"register {username} {licensePlateNumber}":
# 	The system only supports one car per user at the moment, so if a user tries to register another license plate,
# using the same username, the system should print:
# "ERROR: already registered with plate number {licensePlateNumber}"
# 	If the aforementioned checks passes successfully, the plate can be registered, so the system should print:
#  "{username} registered {licensePlateNumber} successfully"
# 	"unregister {username}":
# 	If the user is not present in the database, the system should print:
# "ERROR: user {username} not found"
# 	If the aforementioned check passes successfully, the system should print:
# "{username} unregistered successfully"
# After you execute all of the commands, print all the currently registered users and their license plates in the format:
# 	"{username} => {licensePlateNumber}"
# Input
# 	First line: n – number of commands – integer
# 	Next n lines: commands in one of the two possible formats:
# 	Register: "register {username} {licensePlateNumber}"
# 	Unregister: "unregister {username}"
# The input will always be valid and you do not need to check it explicitly.
car_dict = {}
n = int(input())
for times in range(0 , n):
	command = input().split()
	if command[0] == "register":
		_, name, licensePlateNumber = command
		if name in car_dict:
			print(f'ERROR: already registered with plate number {licensePlateNumber}')
		else:
			car_dict[name] = licensePlateNumber
			print(f'{name} registered {licensePlateNumber} successfully')

	elif command[0] == "unregister":
		_, name = command
		if name not in car_dict:
			print(f'ERROR: user {name} not found')
		else:
			print(f'{name} unregistered successfully')
			car_dict.pop(name)

for name , number in car_dict.items():
	print(f'{name} => {number}')



