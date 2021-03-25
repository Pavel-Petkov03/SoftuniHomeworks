# There is a party at SoftUni. Many guests are invited and there are two types of them:
# Regular and VIP. When a guest comes, check if he/she exists in any of the two reservation lists.
# All reservation numbers are 8 characters long and all VIP numbers will start with a digit.
# First, you will be receiving the number of guests and their reservation numbers.
# After that, you will be receiving guests, who came to the party, until you receive
# the "END" command:
# In the end, print the count of the guests who didn't come to the party and their
# reservation numbers. The VIP guests must be first.
# Both the VIP and the Regular guests must be sorted in ascending order.


reservation_set = {input() for c in range(int(input()))}
coming_set = set()
command = input()
while command != 'END':
	coming_set.add(command)
	command = input()
print(len(reservation_set.difference(coming_set)))
print('\n'.join(sorted(reservation_set.difference(coming_set))))
