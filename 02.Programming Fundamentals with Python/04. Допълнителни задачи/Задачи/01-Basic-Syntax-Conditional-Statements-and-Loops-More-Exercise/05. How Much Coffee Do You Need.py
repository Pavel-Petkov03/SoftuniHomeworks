# Everybody knows that you passed to much time awake during night time...
# Your task is to define how much coffee you need to stay awake after your night.
# Until you receive the command "END", you need to read a single command.
# According to this command you will print the number of coffee you need to stay awake during day time.
# Note: If the count exceeds 5 please return 'You need extra sleep'.
# The list of events can contain the following:
# •	You have homework to do ('coding').
# •	You have a dog or a cat that just decided to wake up too early ('dog' or 'cat').
# •	You just watch a movie ('movie').
# •	Other events can be present and it will be represent by arbitrary string, just ignore this one.
# Each event can be lowercase, or uppercase.
# If it is lowercase you need 1 coffee by event and if it is uppercase you need 2 coffees.
command = input()
coffee = 0
is_sleep = False
while command != "END":
    if command.islower() and command.lower() == "coding":
        coffee += 1
    elif command.isupper() and command.lower() == "coding":
        coffee += 2
    if command.islower() and (command.lower() == "dog" or command.lower() == "cat"):
        coffee += 1
    elif command.isupper() and (command.lower() == "dog" or command.lower() == "cat"):
        coffee += 2
    if command.islower() and command.lower() == "movie":
        coffee += 1
    elif command.isupper() and command.lower() == "movie":
        coffee += 2
    if coffee > 5:
        is_sleep = True
        break
    command = input()
if is_sleep:
    print("You need extra sleep")
else:
    print(coffee)
