# Write a program that:
# •	Records a car number for every car that enters the parking lot
# •	Removes a car number when the car leaves the parking lot
# The input will be the number of commands, which you will receive, and cars in the format:
# direction, car_number. Print the car numbers, which are still in the parking lot.
# NOTE: The order in which we print the result does not matter.


a = set()
for c in range(int(input())):
	cmd, number = input().split(', ')
	if cmd == 'IN':
		a.add(number)
	else:
		a.remove(number)

if a:
	print('\n'.join(a))
else:
	print('Parking Lot is Empty')
