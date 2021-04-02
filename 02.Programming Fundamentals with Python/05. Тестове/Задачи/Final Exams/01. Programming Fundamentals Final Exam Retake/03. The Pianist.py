# You are a pianist and you like to keep a list of your favorite piano pieces. Create a program,
# to help you organize it and add, change, remove pieces from it!
# On the first line of the standard input you will receive an integer n – the number of pieces
# that you will initially have. On the next n lines the pieces themselves will follow with their
# composer and key, separated by "|" in the following format:
# {piece}|{composer}|{key}
# Then, you will be receiving different commands, each on a new line, separated by
# "|", until the "Stop" command is given:
# •	Add|{piece}|{composer}|{key}
# o	You need to add the given piece with the information about it to the other pieces
# o	If the piece is already in the collection, print:
# "{piece} is already in the collection!"
# o	If the piece is not in the collection, print:
# "{piece} by {composer} in {key} added to the collection!"
# •	Remove|{piece}
# o	If the piece is in the collection, remove it and print:
# "Successfully removed {piece}!"
# o	If the piece is not in the collection, print:
# "Invalid operation! {piece} does not exist in the collection."
# •	ChangeKey|{piece}|{new key}
# o	If the piece is in the collection, change its key with the given one and print:
# "Changed the key of {piece} to {new key}!"
# o	If the piece is not in the collection, print:
# "Invalid operation! {piece} does not exist in the collection."
# Upon receiving the "Stop" command you need to print all pieces in your collection,
# sorted by their name and by the name of their composer in alphabetical order, in the following format:
# "{Piece} -> Composer: {composer}, Key: {key}"
# Input/Constraints
# •	You will receive a single integer at first – the initial number of pieces in the collection
# •	For each piece you will receive a single line of text with information about it.
# •	Then you will receive multiple commands in the way described above, until the command "Stop".
# Output
# •	All the output messages with the appropriate formats are described in the problem description.

pattern_dict = {}
n = int(input())
for t in range(n):
    piece, composer, key = input().split("|")
    pattern_dict[piece] = [composer, key]

command = input()
while command != 'Stop':
    command = command.split("|")
    if command[0] == 'Add':
        _, piece, composer, key = command
        if piece in pattern_dict:
            print(f'{piece} is already in the collection!')
        else:
            print(f'{piece} by {composer} in {key} added to the collection!')
            pattern_dict[piece] = [composer, key]
    elif command[0] == 'Remove':
        _, piece = command
        if piece in pattern_dict:
            pattern_dict.pop(piece)
            print(f'Successfully removed {piece}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')
    elif command[0] == 'ChangeKey':
        _, piece, new_key = command
        if piece in pattern_dict:
            pattern_dict[piece][1] = new_key
            print(f'Changed the key of {piece} to {new_key}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')
    command = input()

for key, value in sorted(pattern_dict.items(), key=lambda x: (x[0], x[1][0])):
    print(f'{key} -> Composer: {value[0]}, Key: {value[1]}')
