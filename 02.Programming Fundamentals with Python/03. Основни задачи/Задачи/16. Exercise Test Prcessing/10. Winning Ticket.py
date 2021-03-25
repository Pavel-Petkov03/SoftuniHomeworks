# Lottery is exciting. What is not, is checking a million tickets for winnings only by hand. So, you are given the
# task to create a program which automatically checks if a ticket is a winner.
# You are given a collection of tickets separated by commas and spaces. You need to check every one of them
# if it has a winning combination of symbols.
# A valid ticket should have exactly 20 characters. The winning symbols are '@', '#', '$' and '^'. But in order
# for a ticket to be a winner the symbol should uninterruptedly repeat for at least 6 times in both the tickets
# left half and the tickets right half.
# For example, a valid winning ticket should be something like this:
# "Cash$$$$$$Ca$$$$$$sh"
# The left half "Cash$$$$$$" contains "$$$$$$", which is also contained in the tickets right half "Ca$$$$$$sh".
# A winning ticket should contain symbols repeating up to 10 times in both halves, which is considered a Jackpot
# (for example: "$$$$$$$$$$$$$$$$$$$$").
# Input
# The input will be read from the console. The input consists of a single line containing all tickets separated by
# commas and one or more white spaces in the format:
# •	"{ticket}, {ticket}, … {ticket}"
# Output
# Print the result for every ticket in the order of their appearance, each on a separate line in the format:
# •	Invalid ticket - "invalid ticket"
# •	No match - "ticket "{ticket}" - no match"
# •	Match with length 6 to 9 - "ticket "{ticket}" - {match length}{match symbol}"
# •	Match with length 10 - "ticket "{ticket}" - {match length}{match symbol} Jackpot!"
# Constrains
# •	Number of tickets will be in range [0 … 100]

def jackpot(left, right, match):
	for char in match:
		if char * 10 in left and char * 10 == right:
			print( f'ticket "{ticket}" - 10{char} Jackpot!' )
			return True
	return False


def win(left, right, match):
	for char in match:
		if char * 6 in left and char * 6 in right:
			print( f'ticket "{ticket}" - {min(left.count(char), right.count(char))}{char}')
			return True
	return False


matching_list = ['@','#','$','^']
tickets = input().split(", ")
for ticket in tickets:
	ticket = ticket.strip()
	if len(ticket) == 20:
		left_side = ticket[0:10]
		right_side = ticket[10:]
		if jackpot(left_side, right_side, matching_list):
			continue
		elif win(left_side , right_side , matching_list):
			continue
		else:
			print(f'ticket "{ticket}" - no match')

	else:
		print("invalid ticket")












