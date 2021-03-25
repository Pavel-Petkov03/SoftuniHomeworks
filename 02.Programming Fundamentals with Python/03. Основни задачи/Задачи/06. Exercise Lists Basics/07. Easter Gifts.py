# As a good friend, you decide to buy presents for your friends.
# Create a program that helps you plan the gifts for your friends and family.
# First, you are going to receive the gifts you plan on buying on a single
# line, separated by space, in the following format:
# "{gift1} {gift2} {gift3}… {giftn}"
# Then you will start receiving commands until you read the "No Money" message. There are three possible commands:
# •	"OutOfStock {gift}"
# o	Find the gifts with this name in your collection, if there are any, and change their values to "None".
# •	"Required {gift} {index}"
# o	Replace the value of the current gift on the given index with this gift, if the index is valid.
# •	"JustInCase {gift}"
# o	Replace the value of your last gift with this one.
# In the end, print the gifts on a single line, except the ones with value
# "None", separated by a single space in the following format:
# "{gift1} {gift2} {gift3}… {giftn}"
# Input / Constraints
# •	On the 1st line you are going to receive the names of the gifts, separated by a single space.
# •	On the next lines, until the "No Money" command is received, you will be receiving commands.
# •	The input will always be valid.
gifts = input().split()
command = input()
while command != "No Money":
    command = command.split()
    if command[0] == "OutOfStock" and command[1] in gifts:
        for c in range(gifts.count(command[1])):
            idx = gifts.index(command[1])
            gifts[idx] = None
    elif command[0] == "Required" and 0 <= int(command[2]) < len(gifts):
        gifts[int(command[2])] = command[1]
    elif command[0] == "JustInCase":
        gifts[-1] = command[1]
    command = input()
print(" ".join(filter(None, gifts)))


