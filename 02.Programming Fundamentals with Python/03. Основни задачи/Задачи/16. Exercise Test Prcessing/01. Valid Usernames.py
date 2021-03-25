# Write a program that reads user names on a single line (joined by ", ") and prints all valid usernames.
# A valid username is:
# •	Has length between 3 and 16 characters
# •	Contains only letters, numbers, hyphens and underscores
# •	Has no redundant symbols before, after or in between

username = input().split(", ")

for user in username:
	is_true = False
	if 3 <=len(user) <= 16:
		for char in user:
			if ord(char) == 45 or ord(char) == 95 or 65 <= ord(char) <= 90 or 48 <= ord(char) <= 57 or 97 <= ord(char) <= 122:
				is_true = True
			else:
				is_true = False
				break
		if is_true:
			print(user)

