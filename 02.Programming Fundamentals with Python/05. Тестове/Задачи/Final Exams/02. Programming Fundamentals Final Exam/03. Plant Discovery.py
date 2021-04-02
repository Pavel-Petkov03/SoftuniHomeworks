# Problem 3. Plant Discovery
# You have now returned from your world tour. On your way you have discovered some new plants and you want to
# gather some information about them and create an exhibition to see which plant is highest rated.
# On the first line you will receive a number n. On the next n lines, you will be given some information about
# the plants that you have discovered in the format: "{plant}<->{rarity}". Store that information, because you
# will need it later. If you receive a plant more than once, update its rarity.
# After that until you receive the command "Exhibition" you will be given some of these commands:
# •	Rate: {plant} - {rating} – add the given rating to the plant (store all ratings)
# •	Update: {plant} - {new_rarity} – update the rarity of the plant with the new one
# •	Reset: {plant} – remove all the ratings of the given plant
# Note: If any of the command is invalid, print "error"
# After the command "Exhibition" print the information that you have about the plants in the following format:
# Plants for the exhibition:
# - {plant_name}; Rarity: {rarity}; Rating: {average_rating formatted to the 2nd digit}
# …
# The plants should be sorted by rarity descending, then by average rating descending
# Input / Constraints
# •	You will recive the input as described above
# •	JavaScript: you will receive a list of strings
# Output
# •	Print the information about all plants as described above

our_dict = {}
for c in range(int(input())):
    key, rarity = input().split("<->")
    our_dict[key] = [int(rarity), []]

command = input()
while command != 'Exhibition':
    task, doing = command.split(': ')
    if task == 'Rate':
        p, r = doing.split(" - ")
        if p in our_dict:
            our_dict[p][1].append(int(r))
        else:
            print('error')
    elif task == 'Update':
        p, new_rarity = doing.split(" - ")
        if p in our_dict:
            our_dict[p][0] = int(new_rarity)
        else:
            print('error')
    elif task == 'Reset':
        p = doing
        if p in our_dict:
            our_dict[p][1].clear()
        else:
            print('error')

    command = input()
new = {}
print('Plants for the exhibition:')
for key, value in our_dict.items():
    if len(our_dict[key][1]) != 0:
        average = sum([c for c in our_dict[key][1]]) / len(our_dict[key][1])
    else:
        average = 0

    new[key] = [value[0], average]

for key, value in sorted(new.items(), key=lambda z: (-z[1][0], -z[1][1])):
    print(f'- {key}; Rarity: {value[0]}; Rating: {value[1]:.2f}')
