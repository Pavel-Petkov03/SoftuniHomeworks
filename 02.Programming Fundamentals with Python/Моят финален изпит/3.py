our_dict = {}
command = input()
while command != 'Log out':
    command = command.split(': ')
    if command[0] == 'New follower':
        # [] -. likes - comments
        if command[1] not in our_dict:
            our_dict[command[1]] = [0, 0]
    if command[0] == 'Like':
        _, username, count = command
        if username in our_dict:
            our_dict[username][0] += int(count)
        else:
            our_dict[username] = [int(count), 0]
    if command[0] == 'Comment':
        _, username = command
        if username in our_dict:
            our_dict[username][1] += 1
        else:
            our_dict[username] = [0, 1]
    if command[0] == 'Blocked':
        _, delete = command
        if delete in our_dict:
            our_dict.pop(delete)
        else:
            print(f"{delete} doesn't exist.")
    command = input()

print(f'{len(our_dict)} followers')
for user, likes_and_comments in sorted(our_dict.items(), key=lambda x: (-(x[1][0] + x[1][1]), x[0])):
    print(f'{user}: {likes_and_comments[0] + likes_and_comments[1]}')
